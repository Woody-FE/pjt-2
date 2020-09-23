<template>
	<section class="profileInfo-wrap">
		<img class="profileInfo-img" :src="profileImageSrc" alt="profileImg" />
		<p class="profileInfo-name">{{ userData.name }}</p>
		<section class="btn-box">
			<router-link to="/profile/modifyinfo">
				<button class="btn-update__img btn">정보수정</button>
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
import { getUserProfile, changeImage, resetImage } from '@/api/profile';
export default {
	data() {
		return {
			userData: {
				name: null,
				imgPath: null,
			},
		};
	},
	methods: {
		async fetchData() {
			try {
				const id = this.$store.getters.getId;
				const { data } = await getUserProfile(id);
				console.log(data);
				this.userData.name = data.username;
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
				await this.patchImage(changeImage);
				this.fetchData();
				alert('프로필이 변경 되었어요');
			} catch (error) {
				console.log(error);
			}
		},
		async resetProfile() {
			try {
				const id = this.$store.getters.getId;
				await resetImage(id);
				this.fetchData();
				alert('프로필이 초기화 되었어요');
			} catch (error) {
				console.log(error);
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
		margin-bottom: 1rem;
		border-radius: 50%;
		border: 1px solid yellow;
	}
	.profileInfo-name {
		font-size: 3rem;
		margin-bottom: 1.5rem;
	}
	.btn-box {
		display: flex;
		margin-bottom: 3rem;
		.btn {
			width: 100px;
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
