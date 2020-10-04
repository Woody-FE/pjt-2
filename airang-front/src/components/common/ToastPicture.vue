<template>
	<section class="toast" :class="toastAnimationClass">
		<img src="" alt="" />
		<h2 class="toast-title">책을 저장하시겠습니까 ?</h2>
		<section>
			<button class="toast-btn-white" @click="closeToast">취소</button>
			<button class="toast-btn-purple" @click="showToast">저장</button>
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
		openMethod({ mystory, job, selectStories }) {
			this.mystory = mystory;
			this.selectStories = selectStories;
			this.job = job;
			this.open = true;
		},
		async showToast() {
			console.log(this.mystory, this.job, this.selectStories);
			await finishedMyStory(this.mystory, this.job, this.selectStories);
			this.open = false;
			this.$router.push({ name: 'bookshelf' });
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
	color: white;
	top: 50%;
	left: 50%;
	display: flex;
	flex-direction: column;
	justify-content: center;
	align-items: center;
	transform: translate(-50%, -50%);
	.toast-title {
		font-size: 3rem;
	}
}
.toast.none {
	display: none;
}
.toast-btn-white {
	border: none;
	width: 7rem;
	border-radius: 3px;
	padding: 0 1rem;
	font-size: 2rem;
	font-weight: 700;
	background: white;
	color: black;
	height: 4rem;
	margin-top: 1.5rem;
	margin-right: 0.5rem;
	cursor: pointer;
	z-index: 2;
}
.toast-btn-purple {
	border: none;
	border-radius: 3px;
	width: 7rem;
	padding: 0 1rem;
	font-size: 2rem;
	font-weight: 700;
	background: $orange;
	color: white;
	height: 4rem;
	margin-top: 1.5rem;
	margin-left: 0.5rem;
	cursor: pointer;
	z-index: 2;
}
</style>
