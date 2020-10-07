<template>
	<section class="toast" :class="toastAnimationClass">
		<img class="toast-img" src="@/assets/images/bg/selectBg.png" alt="" />
		<h2 class="toast-title">책을 저장하시겠습니까 ?</h2>
		<section class="toast-btn">
			<button class="toast-btn-white btn" @click="closeToast">취소</button>
			<button class="toast-btn-purple btn" @click="showToast">저장</button>
		</section>
	</section>
</template>
<script>
import bus from '@/utils/bus.js';
import { finishedMyStory } from '@/api/story';
export default {
	data() {
		return {
			open: false,
			message: '',
			mystory: null,
			selectStories: null,
			job: null,
		};
	},
	computed: {
		toastAnimationClass() {
			return this.open ? null : 'none';
		},
	},
	methods: {
		openMethod({ mystory, job, selectStories, defaultImage }) {
			this.mystory = mystory;
			this.selectStories = selectStories;
			this.job = job;
			this.defaultImage = defaultImage;
			this.open = true;
		},
		async showToast() {
			await finishedMyStory(
				this.mystory,
				this.job,
				this.selectStories,
				this.defaultImage,
			);

			this.open = false;
			this.$router.push({ name: 'profile' });
		},
		closeToast() {
			this.open = false;
			this.$router.push({ name: 'bookshelf' });
		},
	},
	created() {
		bus.$on('show:finished', this.openMethod);
	},
	beforeDestroy() {
		bus.$off('show:finished', this.openMethod);
	},
	watch: {
		$route() {
			this.open = false;
		},
	},
};
</script>
<style lang="scss" scoped>
@include common-btn();
.toast {
	position: fixed;
	width: 100vw;
	/* @media screen and (max-width: 640px) {
		width: 500px;
	} */
	height: 100vh;
	background: white;
	color: black;
	border-radius: 4px;
	box-shadow: 0 8px 20px 0 rgba(0, 0, 0, 0.2);
	color: #343a40;
	top: 50%;
	left: 50%;
	display: flex;
	flex-direction: column;
	justify-content: center;
	align-items: center;
	transform: translate(-50%, -50%);
	.toast-title {
		z-index: 1;
		font-size: 3rem;
	}
	.toast-img {
		z-index: 1;
		position: absolute;
		width: 700px;
		height: 400px;
		top: 50%;
		left: 50%;
		transform: translate(-50%, -50%);
	}
}
.toast.none {
	display: none;
}
.toast-btn {
	z-index: 2;
	margin-top: 3rem;
}
.toast-btn-white {
	width: 7rem;
	padding: 0 1rem;
	font-size: 2rem;
	font-weight: 700;
	background: white;
	color: $deepGray;
	height: 4rem;
	margin-right: 0.5rem;
	cursor: pointer;
}
.toast-btn-purple {
	width: 7rem;
	padding: 0 1rem;
	font-size: 2rem;
	font-weight: 700;
	background: #204c75;
	color: white;
	height: 4rem;
	margin-left: 0.5rem;
	cursor: pointer;
}
</style>
