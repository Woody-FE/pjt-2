<template>
	<section class="book-wrap">
		<img
			src="@/assets/images/default_book.jpg"
			class="book-pace"
			alt="book-pace"
		/>
		<span class="book-name">{{ book.story_name }}</span>
		<img :src="enddingRoot" class="book-img" alt="endding-img" />
	</section>
</template>

<script>
import { mapGetters } from 'vuex';
export default {
	props: {
		book: Object,
	},
	computed: {
		...mapGetters(['getId']),
		enddingRoot() {
			const baseURL = process.env.VUE_APP_API_URL;
			const enddingNum = this.book.finished;
			const storyId = this.book.id;
			const userId = this.getId;
			return `${baseURL}images/user/${userId}/mystory/${storyId}/${enddingNum}.png`;
		},
	},
};
</script>

<style lang="scss" scoped>
.book-wrap {
	position: relative;
	width: 100%;
	height: 100%;
	.book-name {
		width: 100%;
		position: absolute;
		font-size: 1.2rem;
		bottom: 84%;
		color: black;
		margin-left: 13%;
		@media screen and (max-width: 1024px) {
			font-size: 0.9rem;
		}
		@media screen and (max-width: 768px) {
			font-size: 0.6rem;
		}
	}
	.book-pace {
		width: 100%;
		height: 100%;
		position: absolute;
	}
	.book-img {
		position: absolute;
		bottom: 45%;
		left: 50%;
		width: 38%;
		transform: translate(-50%, 50%);
	}
}
</style>
