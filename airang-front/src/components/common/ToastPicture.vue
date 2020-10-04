<template>
	<section class="toast" :class="toastAnimationClass">
		<h2>책을 저장하시겠습니까 ?</h2>
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
		};
	},
	computed: {
		toastAnimationClass() {
			return this.open ? null : 'none';
		},
	},
	methods: {
		openMethod({ mystory, selectStories }) {
			this.mystory = mystory;
			this.selectStories = selectStories;
			this.open = true;
		},
		async showToast() {
			await finishedMyStory(this.mystory, this.selectStories);
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
	/* width: 600px; */
	width: 100vw;
	@media screen and (max-width: 640px) {
		width: 500px;
	}
	/* height: 600px; */
	height: 100vh;
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
