<template>
	<section class="bookshelf-wrap">
		<h2>아이랑 도서관</h2>
		<div class="bookshelf">
			<div class="bookshelf-books">
				<div class="bookshelf-book" :key="book.id" v-for="book in books">
					<router-link :to="`/bookshelf/${book.id}`"
						><div
							class="book books-1"
							v-bind:style="{
								backgroundImage: `url('${imgSrc}${filterMedia(
									book.cover_image,
								)}')`,
							}"
						></div>
					</router-link>
				</div>
			</div>
		</div>
	</section>
</template>

<script>
import { fetchStories } from '@/api/story';
export default {
	created() {
		this.fetchBooks();
	},
	data() {
		return {
			books: [],
		};
	},
	computed: {
		imgSrc() {
			return process.env.VUE_APP_API_URL;
		},
	},
	watch: {
		$route() {
			this.fetchBooks();
		},
	},
	methods: {
		async fetchBooks() {
			try {
				const { data } = await fetchStories();
				this.books = data;
				console.log(data);
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
	},
};
</script>

<style lang="scss" scoped>
.bookshelf-wrap {
	width: 100%;
	height: 100%;
	display: flex;
	flex-direction: column;
	justify-content: center;
	h2 {
		font-size: 24px;
		border-left: 2px solid yellow;
		padding-left: 5px;
	}
}
.bookshelf-books {
	width: 100%;
	height: 100%;
	display: flex;
	flex-wrap: wrap;

	.bookshelf-book {
		width: 33%;
		display: flex;
		justify-content: center;
		align-items: center;
		margin: 1rem 0;
	}
}
@include Book();
.book-add__btn {
	width: 60px;
	height: 35px;
	background-color: rgba(20, 148, 33, 0.8);
	color: white;
	border: none;
	border-radius: 8px;
	cursor: pointer;
	&:hover {
		background-color: rgba(20, 148, 33, 1);
	}
}
</style>
