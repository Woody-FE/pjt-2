<template>
	<section class="bookshelf-wrap">
		<h2>아이랑 도서관</h2>
		<div class="box-out">
			<div :key="book.id" v-for="book in books">
				<router-link
					v-if="book.finished"
					:to="`/story/${book.story.id}/review/${book.id}/`"
					><div
						class="book books-1"
						v-bind:style="{
							backgroundImage: `url('${imgSrc}${filterMedia(
								book.story.cover_image,
							)}')`,
						}"
					></div>
				</router-link>
			</div>
		</div>
		<div>
			<button class="book-add__btn" @click="createBook">책 생성</button>
		</div>
	</section>
</template>

<script>
import { createMyStory, fetchMyStories } from '@/api/story';
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
				const { data } = await fetchMyStories();
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

		async createBook() {
			try {
				if (this.books.length < 4) {
					const { data } = await createMyStory({
						story_id: 1,
						story_name: '세가지 선물',
					});
					this.$router.push(`/story/${data.story.id}/${data.id}/`);
				} else {
					alert('생성하신 책이 많습니다');
				}
			} catch (error) {
				console.log(error);
			}
		},
	},
};
</script>

<style lang="scss" scoped>
.bookshelf-wrap {
	margin: 0 auto;
	position: relative;
	h2 {
		position: absolute;
		top: 90px;
		font-size: 24px;
		border-left: 2px solid yellow;
		padding-left: 5px;
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
