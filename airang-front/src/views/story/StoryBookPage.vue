<template>
	<section class="mystory-wrap__white" v-if="mainLoading">
		<img class="mystory-loading" src="@/assets/images/loading.gif" alt="" />
		<span class="mystory-loading__description">책을 만들고 있어요</span>
	</section>
	<section v-else class="mystory-wrap">
		<div class="mystory-bookcover">
			<section class="mystory-page">
				<div class="mystory-face mystory-cover">
					<img v-if="cover" class="mystory-cover__img" :src="coverSrc" alt="" />
				</div>
				<div class="mystory-face">
					<section class="mystory-select">
						<img
							class="mystory-select__bg"
							src="@/assets/images/bg/selectBg.png"
							alt=""
						/>
						<img
							class="mystory-select__leftimg"
							src="@/assets/images/character/selectArang.png"
							alt=""
						/>

						<button
							class="mystory-select__btn btn"
							@click="
								nexts();
								nextPage();
							"
						>
							책 생성
						</button>
					</section>
				</div>
			</section>
			<section class="mystory-page">
				<div class="mystory-face mystory-select">
					<img
						class="mystory-select__bg"
						src="@/assets/images/bg/selectBg2.png"
						alt=""
					/>
					<img
						class="mystory-select__rightimg"
						src="@/assets/images/character/selectArang2.png"
						alt=""
					/>
					<button
						class="mystory-select__btn btn"
						@click="$router.push('/profile')"
					>
						책 보기
					</button>
				</div>
				<div class="mystory-face mystory-description">
					<div class="mystory-portrait">
						<div class="portrait-box">
							<img
								class="left-img"
								src="@/assets/images/bg/house1.jpg"
								alt=""
							/>
							<img
								src="@/assets/images/character/nukkied_eating.png"
								alt=""
								class="left-arang"
							/>
							<img
								src="@/assets/images/bg/selectBg.png"
								alt=""
								class="left-pink"
							/>
							<p class="left-say">
								여행을 가기 전 아버지가 <br />
								나에게 세 가지 선물을 줬어,<br />
								이 선물들과 함께 <br />
								내가 되고 싶은 모습을 찾을거야!
							</p>
							<!-- <p class="portrait-name">
								줄거리
							</p> -->
							<p class="portrait-content"></p>
						</div>
					</div>
				</div>
			</section>
			<section class="mystory-page">
				<div class="mystory-face mystory-input">
					<div class="mystory-bookinfo">
						<label class="mystory-label" for="bookname">책 이름</label>
						<input
							:placeholder="defaultBookname"
							class="mystory-bookname"
							id="bookname"
							type="text"
							v-model="bookName"
						/>
					</div>
					<section v-if="loading" class="mystory-imgbox">
						<img
							class="mystory-imgbox__loading"
							src="@/assets/images/loading.gif"
							alt=""
						/>
						<span class="mystory-imgbox__description">
							사진을 만들고 있어요
						</span>
					</section>
					<section v-else class="mystory-imgbox">
						<img
							class="mystory-imgbox__img"
							:src="`${changeImageSrc}${new Date()}`"
							alt="profileImg"
						/>
						<section class="mystory-imgbtn">
							<button type="button" class="mystory-imgbtn__btn btn">
								사진수정<input
									ref="inputFile"
									id=""
									type="file"
									accept="image/*"
									@change="onChangeFile"
									class="fake-btn"
								/>
							</button>
							<button
								@click="defaultImage"
								type="button"
								class="mystory-imgbtn__btn btn"
							>
								기본사진
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
import bus from '@/utils/bus';
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
			myFicture: false,
			cnt: 0,
			count: 0,
			mainLoading: false,
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
				? `${this.imgSrc}${this.conversionImage}?count=${new Date()}`
				: `${this.imgSrc}images/character/nukkied_default2.png?`;
		},
	},
	updated() {
		const cover = document.querySelector('.mystory-cover__img');
		if (cover) {
			cover.addEventListener('load', () => {
				const page = document.querySelectorAll('.mystory-page');
				setTimeout(function() {
					page[0].classList.add('flipped');
				}, 750);
			});
		}
	},
	methods: {
		nexts() {
			const Btn = document.querySelector('.btn');
			Btn.style.opacity = 'none';
			const face = document.querySelectorAll('.mystory-face');
			face[3].style.trasform = 'rotateY(-180deg)';
		},
		nextPage() {
			const page = document.querySelectorAll('.mystory-page');
			page[1].style.zIndex = 4;
			page[1].classList.add('flipped');
		},
		async fetchData() {
			try {
				const { data } = await getUserProfile(this.userId);
				this.userData.imgPath = data.child_image;
				if (this.userData.imgPath) {
					this.createImage();
				}
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
				} else {
					bus.$emit(
						'show:warning',
						'.jpg, .jpeg, .png형태의 파일을 넣어주세요',
					);
				}
			} catch (error) {
				console.log(error);
			}
		},
		async fetchStoryBook() {
			try {
				this.mainLoading = true;
				const { data } = await fetchStory(this.storyId);
				this.cover = data.cover_image;
				this.defaultBookname = data.name;
				this.mainLoading = false;
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
				const { data } = await convertImage(this.userId);
				this.conversionImage = data.path;
				this.myFicture = true;
			} catch (error) {
				this.conversionImage = null;
				bus.$emit('show:warning', error.response.data.detail);
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
				if (this.myFicture) {
					this.$router.push(`/story/${data.story.id}/${data.id}`);
				} else {
					this.$router.push(`/story/${data.story.id}/${data.id}?default=true`);
				}
			} catch (error) {
				console.log(error);
			}
		},
		defaultImage() {
			this.myFicture = false;
			this.conversionImage = false;
		},
	},
};
</script>

<style lang="scss" scoped>
@include common-btn();
.mystory-wrap__white {
	width: 100%;
	min-height: 100vh;
	background: white;
	display: flex;
	flex-direction: column;
	justify-content: center;
	align-items: center;
	color: black;
	.mystory-loading {
		width: 20%;
		margin-bottom: 1rem;
	}
	.mystory-loading__description {
		font-size: 2rem;
	}
}
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
		.mystory-page {
			position: absolute;
			left: 50%;
			top: 0;
			box-shadow: 0 2px 6px 0 rgba(68, 67, 68, 0.4);
			width: 50%;
			height: 100%;
			transform-style: preserve-3d;
			transition: 1s;
			border: 1px solid lightgray;
			.mystory-face {
				position: absolute;
				left: 0;
				box-shadow: 0 2px 6px 0 rgba(68, 67, 68, 0.4);
				top: 0;
				width: 100%;
				height: 100%;
				background: white;
				color: black;
				backface-visibility: hidden;
			}
			&:nth-child(1) {
				z-index: 3;
				transform-origin: left;
			}
			&:nth-child(2) {
				z-index: 2;
				transform-origin: left;
			}
			&:nth-child(3) {
				z-index: 1;
			}

			.mystory-description {
				display: flex;
				align-items: center;
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
					}
				}
				.mystory-imgbox {
					width: 100%;
					height: 80%;
					display: flex;
					flex-direction: column;
					align-items: center;
					@media (max-width: 768px) {
						justify-content: center;
					}
					.mystory-imgbox__loading {
						margin-top: 5rem;
						width: 180px;
					}
					.mystory-imgbox__description {
						margin-top: 1.5rem;
						font-size: 1.5rem;
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
				position: relative;
				width: 100%;
				height: 100%;
				.mystory-select__bg {
					width: 100%;
					height: 100%;
				}
				.mystory-select__leftimg {
					position: absolute;
					width: 40%;
					top: 40%;
					left: 52.5%;
					transform: translate(-50%, -50%);
				}
				.mystory-select__rightimg {
					position: absolute;
					width: 30%;
					top: 40%;
					left: 50%;
					transform: translate(-50%, -50%);
				}
				.mystory-select__btn {
					position: absolute;
					bottom: 20%;
					left: 50%;
					width: 200px;
					height: 100px;
					font-size: 2rem;
					border-radius: 40%;
					transform: translate(-50%, 50%);
					backface-visibility: hidden;
					color: #520909;
					background: cornsilk;
				}
			}
		}
	}
	.mystory-imgbtn__btn {
		position: relative;
		color: #495057;
		width: 35%;
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
.mystory-face:nth-child(2) {
	transform: rotateY(-180deg);
}
.mystory-face:nth-child(4) {
	transform: rotateY(0deg);
}
.flipped {
	transform: rotateY(-180deg);
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

.mystory-portrait {
	width: 100%;
	height: 100%;
	padding: 10%;
	.portrait-box {
		position: relative;
		width: 100%;
		height: 100%;
		display: flex;
		flex-direction: column;
		align-items: center;
		box-sizing: border-box;
		.left-img {
			height: 100%;
			width: 100%;
		}
		.left-arang {
			position: absolute;
			top: 45%;
			left: 85%;
			width: 20%;
			height: 30%;
			transform: translate(-50%, 50%);
		}
		.left-pink {
			position: absolute;
			width: 70%;
			height: 25%;
			top: 65%;
			left: 0%;
		}
		.left-say {
			font-family: 'KOMACON';
			position: absolute;
			top: 69%;
			left: 6%;
			line-height: 1.5;
			font-size: 1.2rem;
			@media screen and (max-width: 1024px) {
				font-size: 0.9rem;
			}
			@media screen and (max-width: 768px) {
				font-size: 0.7rem;
			}
		}
		.portrait-img__box {
			display: flex;
			width: 200px;
			height: 300px;
			justify-content: center;
			align-items: center;
			.portrait-img {
				width: 100%;
				height: auto;
			}
		}
		.portrait-name {
			font-size: 1.5rem;
			margin-bottom: 6rem;
		}
		.portrait-content {
			text-align: center;
			line-height: 1.5;
			font-size: 1.5rem;
		}
	}
}
</style>
