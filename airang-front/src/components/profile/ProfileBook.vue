<template>
	<section class="book-wrap">
		<router-link :to="`/bookshelf/${book.id}`" class="book">
			<img
				src="@/assets/images/default_book.jpg"
				class="book-pace"
				alt="book-pace"
			/>
			<span class="book-name">{{ book.story_name }}</span>
		</router-link>
	</section>
</template>

<script>
export default {
	props: {
		book: Object,
	},
};
</script>

<style lang="scss" scoped>
.book-wrap {
	position: relative;
	width: 100%;
	height: 100%;
	.book {
		width: 100%;
		height: 100%;
		.book-name {
			position: absolute;
			font-size: 1.2rem;
			bottom: 85%;
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
	}
}
</style>
