<template>
	<section class="mystory-wrap">
		<div class="mystory-bookcover">
			<section class="mystory-page">
				<div class="mystory-face mystory-cover">
					<img v-if="cover" class="mystory-cover__img" :src="coverSrc" alt="" />
				</div>
				<div class="mystory-face mystory-select">
					<button class="mystory-select__btn btn" @click="nextPage">
						책 생성
					</button>
				</div>
			</section>
			<section class="mystory-page">
				<div class="mystory-face mystory-select">
					<button
						class="mystory-select__btn btn"
						@click="$router.push('/profile')"
					>
						책 보기
					</button>
				</div>
				<div class="mystory-face">설명</div>
			</section>
			<section class="mystory-page">
				<div class="mystory-face mystory-input">
					<div class="mystory-bookinfo">
						<label class="mystory-label" for="bookname">책 이름</label>
						<input
							class="mystory-bookname"
							id="bookname"
							type="text"
							v-model="bookName"
						/>
					</div>
					<section class="mystory-imgbox">
						<div v-if="loading">로딩</div>
						<img
							v-else
							class="mystory-imgbox__img"
							:src="changeImageSrc"
							alt="profileImg"
						/>
						<section class="mystory-imgbtn">
							<button type="button" class="mystory-imgbth__btn btn">
								사진수정<input
									ref="inputFile"
									id=""
									type="file"
									accept="image/*"
									@change="onChangeFile"
									class="fake-btn"
								/>
							</button>
						</section>
					</section>
					<section class="mystory-createbtn">
						<button @click="createBook" class="mystory-createbtn__btn btn">
							책 만들기
						</button>
					</section>
				</div>
			</section>
		</div>
	</section>
</template>

<script>
import { getUserProfile, changeImage, convertImage } from '@/api/profile';
import { createMyStory, fetchStory } from '@/api/story';
export default {
	created() {
		const id = this.$store.getters.getId;
		this.userId = id;
		this.fetchStoryBook();
		this.fetchData();
	},
	props: {
		storyId: Number,
	},
	data() {
		return {
			cnt: 0,
			loading: false,
			userId: null,
			cover: null,
			defaultBookname: null,
			bookName: null,
			conversionImage: null,
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
				? `${this.imgSrc}images/user/${this.userId}/conversion/0.png`
				: `${this.imgSrc}media/image/child/noProfile.jpg`;
		},
		changeImageSrc() {
			return this.conversionImage
				? `${this.imgSrc}${this.conversionImage}?count=${this.cnt}`
				: `${this.imgSrc}media/image/child/noProfile.jpg`;
		},
	},
	mounted() {
		this.createImage();
	},
	updated() {
		const cover = document.querySelector('.mystory-cover__img');
		if (cover) {
			cover.addEventListener('load', () => {
				const page = document.querySelectorAll('.mystory-page');
				setTimeout(function() {
					page[0].classList.add('flipped');
				}, 1000);
			});
		}
	},
	methods: {
		nextPage() {
			const page = document.querySelectorAll('.mystory-page');
			page[1].style.zIndex = 3;
			setTimeout(function() {
				page[1].classList.add('flipped');
			}, 1000);
		},
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
		validateFile(file) {
			const imageArray = ['image/png', 'image/jpg', 'image/jpeg'];
			if (imageArray.includes(file.type)) return true;
			return false;
		},
		async onChangeFile() {
			try {
				const changeImage = this.$refs.inputFile.files[0];
				const isValidate = await this.validateFile(changeImage);
				if (isValidate) {
					await this.patchImage(changeImage);
					this.fetchData();
					this.createImage();
					// alert('사진이 변경 되었어요');
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
				this.defaultBookname = data.name;
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
		async createImage() {
			try {
				this.loading = true;
				this.cnt += 1;
				const id = this.$store.getters.getId;
				const { data } = await convertImage(id);
				console.log(data);
				this.conversionImage = data.path;
			} catch (error) {
				this.conversionImage = null;
				console.log(error.response.data.detail);
			} finally {
				this.loading = false;
			}
		},
		async createBook() {
			try {
				const { data } = await createMyStory({
					story_id: this.storyId,
					story_name: this.bookName ? this.bookName : this.defaultBookname,
				});
				this.$router.push(`/story/${data.story.id}/${data.id}/`);
			} catch (error) {
				console.log(error);
			}
		},
	},
};
</script>

<style lang="scss" scoped>
@include common-btn();
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
		width: 90vw;
		height: 95vh;
		transform-style: preserve-3d;
		margin: auto;
		.mystory-face:nth-child(2) {
			transform: rotateY(180deg);
		}
		.mystory-face:nth-child(4) {
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
			border: 1px solid lightgray;

			&:nth-child(1) {
				z-index: 2;
				transform-origin: left;
			}
			&:nth-child(2) {
				z-index: 1;
				transform-origin: left;
			}
			&.flipped {
				transform: rotateY(-180deg);
			}
			.mystory-face {
				position: absolute;
				left: 0;
				top: 0;
				width: 100%;
				height: 100%;
				background: white;
				color: black;
				backface-visibility: hidden;
			}
			.mystory-input {
				position: relative;
				display: flex;
				flex-direction: column;
				justify-content: center;
				align-content: center;
				box-sizing: border-box;
				padding: 1rem;
				.mystory-bookinfo {
					width: 100%;
					height: 8%;
					position: relative;
					top: 5%;
					left: 0;
					display: flex;
					flex-direction: column;
					align-items: center;
					.mystory-label {
						position: absolute;
						top: -25%;
						left: 20%;
						background: white;
						color: #495057;
						transform: translateX(-50%);
					}
					.mystory-bookname {
						width: 70%;
						height: 100%;
						box-sizing: border-box;
						padding: 0 1rem;
						border: none;
						text-align: center;
						font-size: 1.5rem;
						border-bottom: 2px solid rgba(158, 83, 33, 0.4);
						/* border-radius: 16px; */
					}
				}
				.mystory-imgbox {
					width: 100%;
					height: 80%;
					display: flex;
					flex-direction: column;
					/* justify-content: center; */
					align-items: center;
					@media (max-width: 768px) {
						justify-content: center;
					}
					.mystory-imgbox__img {
						max-width: 100%;
						height: 80%;
						@media (max-width: 768px) {
							width: 80%;
							height: auto;
						}
					}
					.mystory-imgbtn {
						width: 100%;
						height: 20%;
						display: flex;
						justify-content: center;
						align-items: center;
					}
				}
				.mystory-createbtn {
					width: 100%;
					height: 20%;
					display: flex;
					justify-content: center;
					align-items: center;
					.mystory-createbtn__btn {
						width: 70%;
						height: 60%;
						background: #faad08;
						font-size: 2rem;
					}
				}
			}
			.mystory-select {
				display: flex;
				justify-content: center;
				align-items: center;
				.mystory-select__btn {
					width: 200px;
					height: 100px;
					font-size: 2rem;
					border: none;
					color: #520909;
					background: cornsilk;
				}
			}
		}
	}
	.mystory-imgbth__btn {
		position: relative;
		color: #495057;
		width: 70%;
		height: 60%;
		font-size: 1.5rem;
		.fake-btn {
			cursor: pointer;
			position: absolute;
			top: 0;
			left: 0;
			width: 100%;
			height: 100%;
			opacity: 0;
		}
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
