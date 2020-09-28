<template>
	<section class="toast" :class="toastAnimationClass">
		<section class="toast-img">
			<img
				class="toast-img__box"
				src="@/assets/images/user/children.jpeg"
				alt=""
			/>
			<div class="toast-img__description">
				<h2 class="toast-description__title">사용방법</h2>
				<p>1. 정면을 응시한 사진을 이용해주세요.</p>
				<p>2. 상반신 사진을 이용해주세요.</p>
			</div>
		</section>
		<input ref="imageFile" type="file" />
		<section>
			<button class="toast-btn-white" @click="open = false">취소</button>
			<button class="toast-btn-purple" @click="showToast">변경</button>
		</section>
	</section>
</template>
<script>
import bus from '@/utils/bus.js';
import { changeImage } from '@/api/profile';
export default {
	data() {
		return {
			open: false,
			message: '',
			userId: null,
		};
	},
	computed: {
		toastAnimationClass() {
			return this.open ? null : 'none';
		},
	},
	methods: {
		openMethod(userId) {
			this.userId = userId;
			this.open = true;
		},
		async showToast() {
			const change = this.$refs.imageFile.files[0];
			const formdata = new FormData();
			formdata.append('child_image', change);
			await changeImage(this.userId, formdata);
			this.open = false;
			bus.$emit('show:changeImage');
		},
	},
	created() {
		bus.$on('show:picture', this.openMethod);
	},
	beforeDestroy() {
		bus.$off('show:picture', this.openMethod);
	},
	watch: {
		$route() {
			this.open = false;
		},
	},
};
</script>
<style lang="scss" scoped>
.toast {
	position: fixed;
	width: 600px;
	@media screen and (max-width: 640px) {
		width: 500px;
	}
	height: 600px;
	background-color: #22252e;
	border-radius: 4px;
	box-shadow: 0 8px 20px 0 rgba(0, 0, 0, 0.2);
	color: white;
	top: 50%;
	left: 50%;
	display: flex;
	flex-direction: column;
	justify-content: center;
	align-items: center;
	transform: translate(-50%, -50%);
	.toast-img {
		display: flex;
		align-items: center;
		justify-content: center;
		width: 100%;
		height: 50%;
		.toast-img__box {
			width: 35%;
			height: 100%;
			box-sizing: border-box;
			padding: 1rem;
		}
		.toast-img__description {
			width: 65%;
			height: 100%;
			color: white;
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
}
.toast.none {
	display: none;
}
.toast-btn-white {
	border: none;
	border-radius: 3px;
	padding: 0 1rem;
	font-size: 1rem;
	font-weight: 700;
	background: white;
	color: black;
	height: 2rem;
	margin-top: 1.5rem;
	margin-right: 0.5rem;
}
.toast-btn-purple {
	border: none;
	border-radius: 3px;
	padding: 0 1rem;
	font-size: 1rem;
	font-weight: 700;
	color: white;
	height: 2rem;
	margin-top: 1.5rem;
	margin-left: 0.5rem;
}
</style>
