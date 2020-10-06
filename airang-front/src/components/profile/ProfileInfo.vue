<template>
	<section class="profileInfo-wrap">
		<img class="profileInfo-img" :src="profileImageSrc" alt="profileImg" />
		<div class="name-box">
			<p v-if="whatStatus" class="profileInfo-name">{{ userData.name }}</p>
			<input
				v-else
				type="text"
				class="profileInfo-name__change"
				v-model="userData.name"
				@keydown.enter="clickChangeBtn"
			/>
			<i @click="clickChangeBtn" class="icon ion-md-create change-btn">
				<div class="fake-background"></div>
			</i>
		</div>
		<div class="msg-box">
			<p v-if="!isVaildateName" class="hidden-msg1 msg">
				※ 이름은 공백제외 2~5자 한글입니다.
			</p>
		</div>
		<section class="btn-box">
			<router-link to="/profile/modifyinfo">
				<button class="btn-update__img btn">비밀번호수정</button>
			</router-link>
			<button type="file" class="btn-update__info btn">
				사진수정<input
					ref="inputFile"
					id=""
					type="file"
					accept="image/*"
					@change="onChangeFile"
					class="fake-btn"
				/>
			</button>
			<button type="file" class="btn-update__info btn" @click="resetProfile">
				사진초기화
			</button>
		</section>
	</section>
</template>

<script>
import bus from '@/utils/bus';
import { createVoice } from '@/api/profile';
import {
	getUserProfile,
	changeImage,
	resetImage,
	patchUserName,
} from '@/api/profile';
import { validationName } from '@/utils/validation';
// import { mapMutations } from 'vuex';

export default {
	data() {
		return {
			userData: {
				name: null,
				nameStatus: true,
				imgPath: null,
			},
		};
	},
	methods: {
		// ...mapMutations(['setChildName']),
		async fetchData() {
			try {
				const id = this.$store.getters.getId;
				const { data } = await getUserProfile(id);
				this.userData.name = data.child_name;
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
					bus.$emit('show:toast', '프로필이 변경 되었어요');
				} else {
					bus.$emit(
						'show:warning',
						'.jpg, .jpeg, .png형태의 파일을 넣어주세요!',
					);
				}
			} catch (error) {
				console.log(error);
			}
		},
		async resetProfile() {
			try {
				const id = this.$store.getters.getId;
				await resetImage(id);
				this.fetchData();
				bus.$emit('show:toast', '프로필이 초기화 되었어요');
			} catch (error) {
				console.log(error);
			}
		},
		clickChangeBtn() {
			// true 일때, 인풋박스로 바뀜
			if (this.userData.nameStatus) {
				this.changeStatus();
			}
			// false 일 때, 이름변경 요청을 보내고 input -> fix
			else {
				if (this.isVaildateName) {
					this.changeStatus();
					this.changeName();
				} else {
					bus.$emit('show:warning', '이름은 공백제외 2~5자 한글만 가능합니다.');
				}
			}
		},
		changeStatus() {
			this.userData.nameStatus = !this.userData.nameStatus;
		},
		async changeName() {
			try {
				console.log('시작', new Date());
				const content = {
					child_name: this.userData.name,
				};
				const id = this.$store.getters.getId;
				await patchUserName(id, content);
				bus.$emit('show:toast', '이름이 변경되었어요');
				// this.setChildName(content.child_name);
				this.$store.commit('setChildName', content.child_name);
				await Promise.all([
					createVoice(1, id, 1, 3),
					createVoice(1, id, 2, 3),
					createVoice(1, id, 3, 3),
				]);
				console.log('끝', new Date());
			} catch (error) {
				console.log(error.response);
			}
		},
	},
	computed: {
		baseURL() {
			return process.env.VUE_APP_API_URL;
		},
		profileImageSrc() {
			return this.userData.imgPath
				? `${this.baseURL}${this.userData.imgPath}`
				: `${this.baseURL}media/image/child/noProfile.jpg`;
		},
		whatStatus() {
			return this.userData.nameStatus;
		},
		isVaildateName() {
			const name = this.userData.name;
			return validationName(name);
		},
	},
	created() {
		this.fetchData();
	},
};
</script>

<style lang="scss" scoped>
.profileInfo-wrap {
	display: flex;
	flex-direction: column;
	justify-content: center;
	align-items: center;
	.profileInfo-img {
		width: 15rem;
		height: 15rem;
		margin-top: 2rem;
		margin-bottom: 1.5rem;
		border-radius: 50%;
	}
	.name-box {
		display: flex;
		justify-content: center;
		align-items: center;
		position: relative;
		.profileInfo-name {
			// justify-content: center;
			font-size: 3rem;
			width: 250px;
			text-align: center;
			padding: 1px;
		}
		.profileInfo-name__change {
			height: 3rem;
			width: 200px;
			margin-left: 25px;
			margin-right: 25px;
			font-size: 1.5rem;
			border: none;
			border-radius: 1rem;
			text-align: center;
			opacity: 0.6;
			&:focus {
				opacity: 1;
			}
		}
	}
	.change-btn {
		position: absolute;
		right: -3rem;
		top: 50%;
		transform: translate(-50%, -50%);
		font-size: 2rem;
		color: white;
		z-index: 999;
		&:hover {
			cursor: pointer;
		}
		&:hover .fake-background {
			transition: opacity 300ms ease-in;
			opacity: 1;
		}
		.fake-background {
			position: absolute;
			top: -3px;
			left: -8px;
			width: 2.5rem;
			height: 2.5rem;
			border-radius: 10px;
			z-index: -1;
			background: $carrotGreen;
			opacity: 0;
			transition: opacity 300ms ease-out;
		}
	}

	.msg-box {
		height: 2rem;
		.msg {
			color: crimson;
			font-size: 0.9rem;
			font-weight: 100;
		}
	}
	.btn-box {
		display: flex;
		margin-bottom: 3rem;
		.btn {
			width: 150px;
			height: 40px;
			color: white;
			font-size: 1rem;
			background: $carrotGreen;
			border-radius: 15px;
			border: none;
			&:hover {
				cursor: pointer;
				background: $green;
			}
		}
		.btn-update__img {
			margin-right: 0.5rem;
		}
		.btn-update__info {
			margin-right: 0.5rem;
			position: relative;
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
}
</style>
