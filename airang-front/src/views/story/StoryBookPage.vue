<template>
	<section class="mystory-wrap">
		<div class="mystory-bookcover">
			<section class="mystory-page">
				<div class="mystory-face mystory-cover">
					<img v-if="cover" class="mystory-cover__img" :src="coverSrc" alt="" />
				</div>
				<div class="mystory-face mystory-inputbox">
					<section class="mystory-inputbox__item mystory-inputbox__sample">
						<img
							class="mystory-sample__img"
							src="@/assets/images/user/children.jpeg"
							alt=""
						/>
						<div class="mystory-sample__description">
							<h2 class="mystory-description__title">사용방법</h2>
							<p>1. 정면을 응시한 사진을 이용해주세요.</p>
							<p>2. 상반신 사진을 이용해주세요.</p>
						</div>
					</section>
					<section class="mystory-inputbox__item mystory-inputbox__ficture">
						<img
							class="mystory-ficture__img"
							:src="profileImageSrc"
							alt="profileImg"
						/>
						<img
							class="mystory-ficture__img"
							:src="profileImageSrc"
							alt="profileImg"
						/>
						<img
							class="mystory-ficture__transimg"
							:src="profileImageSrc"
							alt="profileImg"
						/>
					</section>
					<section class="mystory-inputbox__item mystory-inputbox__btn">
						333
					</section>
				</div>
			</section>
			<section class="mystory-page mystory-bookpage">
				<div class="mystory-face mystory-books">
					<!-- eslint-disable vue/no-use-v-if-with-v-for,vue/no-confusing-v-for-v-if -->
					<div
						class="mystory-book"
						v-if="book.finished"
						:key="book.id"
						v-for="book in books"
					>
						<router-link :to="`/story/${book.story.id}/review/${book.id}`"
							><div
								class="book books-1"
								v-bind:style="{
									backgroundImage: `url('${imgSrc}${filterMedia(
										book.story.cover_image,
									)}')`,
								}"
							></div>
						</router-link>
					</div>
				</div>
			</section>
		</div>
	</section>
</template>

<script>
import { getUserProfile, changeImage } from '@/api/profile';
import { createMyStory, fetchMyStories, fetchStory } from '@/api/story';
export default {
	created() {
		this.fetchStoryBook();
		this.fetchBooks();
		this.fetchData();
	},
	props: {
		storyId: Number,
	},
	data() {
		return {
			books: [],
			cover: null,
			userData: {
				imgPath: null,
			},
		};
	},
	computed: {
		imgSrc() {
			return process.env.VUE_APP_API_URL;
		},
		coverSrc() {
			return `${process.env.VUE_APP_API_URL}${this.filterMedia(this.cover)}`;
		},
		profileImageSrc() {
			return this.userData.imgPath
				? `${this.imgSrc}${this.userData.imgPath}`
				: `${this.imgSrc}media/image/child/noProfile.jpg`;
		},
	},
	watch: {
		$route() {
			this.fetchBooks();
		},
	},
	mounted() {
		const page = document.querySelectorAll('.mystory-page');
		setTimeout(function() {
			page[0].classList.add('flipped');
		}, 1000);
	},
	methods: {
		async fetchData() {
			try {
				const id = this.$store.getters.getId;
				const { data } = await getUserProfile(id);
				this.userData.imgPath = data.child_image;
			} catch (error) {
				console.log(error);
			}
		},
		async patchImage(img) {
			try {
				const id = this.$store.getters.getId;
				const formdata = new FormData();
				formdata.append('child_image', img);
				await changeImage(id, formdata);
			} catch (error) {
				console.log(error);
			}
		},
		async onChangeFile() {
			try {
				const changeImage = this.$refs.inputFile.files[0];
				const isValidate = await this.validateFile(changeImage);
				if (isValidate) {
					await this.patchImage(changeImage);
					this.fetchData();
					alert('사진이 변경 되었어요');
				} else {
					alert('.jpg, .jpeg, .png형태의 파일을 넣어주세요!');
				}
			} catch (error) {
				console.log(error);
			}
		},
		async fetchStoryBook() {
			try {
				const { data } = await fetchStory(this.storyId);
				console.log(data);
				this.cover = data.cover_image;
			} catch (error) {
				console.log(error);
			}
		},
		async fetchBooks() {
			try {
				const { data } = await fetchMyStories();
				this.books = data;
			} catch (error) {
				console.log(error);
			}
		},
		filterMedia(string) {
			if (string.includes('/media/')) {
				return string.replace('/media/', '');
			}
			return string;
		},
		async createBook() {
			try {
				if (this.books.length < 4) {
					const { data } = await createMyStory({
						story_id: 1,
						story_name: '세가지 선물',
					});
					this.$router.push(`/story/${data.story.id}/${data.id}/`);
				} else {
					alert('생성하신 책이 많습니다');
				}
			} catch (error) {
				console.log(error);
			}
		},
	},
};
</script>

<style lang="scss">
.mystory-wrap {
	position: relative;
	width: 100%;
	min-height: 100vh;
	.mystory-bookcover {
		position: absolute;
		left: 0;
		right: 0;
		top: 0;
		bottom: 0;
		width: 80vw;
		height: 90vh;
		transform-style: preserve-3d;
		margin: auto;
		.mystory-face:nth-child(2) {
			transform: rotateY(180deg);
		}
		.mystory-page {
			position: absolute;
			left: 50%;
			top: 0;
			width: 50%;
			height: 100%;
			transform-style: preserve-3d;
			transition: 1.5s;
			box-shadow: 0 2px 6px 0 rgba(68, 67, 68, 0.5);

			&:nth-child(1) {
				z-index: 2;
				transform-origin: left;
			}
			&:nth-child(2) {
				z-index: 1;
			}
			&:nth-child(1).flipped {
				transform: rotateY(-180deg);
			}
			.mystory-face {
				position: absolute;
				left: 0;
				top: 0;
				width: 100%;
				height: 100%;
				/* background: rgba(#fff8dc, 0.8); */
				background: white;
				color: black;
				backface-visibility: hidden;
			}
			.mystory-books {
				width: 100%;
				height: 100%;
				display: flex;
				flex-wrap: wrap;
				.mystory-book {
					width: 50%;
					display: flex;
					justify-content: center;
					align-items: center;
					margin: 0;
				}
			}
			.mystory-inputbox {
				display: flex;
				flex-direction: column;
				justify-content: center;
				align-items: center;
				box-sizing: border-box;
				padding: 1rem;
				.mystory-inputbox__item {
					width: 100%;
					height: 33%;
				}
				.mystory-inputbox__sample {
					display: flex;
					flex-wrap: wrap;
					align-items: center;
					padding: 1rem 0;
					.mystory-sample__img {
						width: 35%;
						height: 100%;
						border-radius: 8px;
					}
					.mystory-sample__description {
						width: 65%;
						height: 100%;
						color: black;
						display: flex;
						flex-direction: column;
						justify-content: center;
						box-sizing: border-box;
						padding-left: 1rem;
						.mystory-description__title {
							text-align: center;
							margin-bottom: 1rem;
						}
					}
				}
				.mystory-inputbox__ficture {
					display: flex;
					flex-wrap: wrap;
					.mystory-ficture__img {
						width: 30%;
						height: 100%;
						/* box-shadow: 0.2rem 0.8rem 1.6rem grey; */
						/* border: 1px solid black; */
						border-radius: 16px;
						margin: 0 auto;
					}
					.mystory-ficture__transimg {
						width: 30%;
						height: 100%;
						/* box-shadow: 0.2rem 0.8rem 1.6rem grey; */
						border-radius: 16px;
						margin: 0 auto;
					}
				}
			}
		}
	}
}
@-webkit-keyframes bookBlock {
	from {
		transform: rotateY(180deg);
	}
	to {
		transform: rotateY(-180deg);
	}
}
.mystory-cover {
	width: 100%;
	display: flex;
	justify-content: center;
	align-items: center;
	.mystory-cover__img {
		width: 100%;
		height: 100%;
		object-fit: fill;
	}
}
@include Book();
</style>
