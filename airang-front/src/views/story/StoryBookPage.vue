<template>
	<section class="mystory-wrap">
		<div class="mystory-bookcover">
			<section class="mystory-page">
				<div class="mystory-inputbox"></div>
			</section>
			<section class="mystory-page mystory-bookpage">
				<div class="box-out">
					<div class="mystory-book" :key="book.id" v-for="book in books">
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
			</section>
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

<style lang="scss">
.mystory-wrap {
	width: 100%;
	height: 100vh;
	display: flex;
	justify-content: center;
	align-items: center;
	.mystory-bookcover {
		background: white;
		width: 80vw;
		height: 80vh;
		display: flex;
		flex-wrap: wrap;
	}
	.mystory-page {
		box-shadow: 0 2px 6px 0 rgba(68, 67, 68, 0.5);
		width: 50%;
		height: 100%;
	}
	.mystory-bookpage {
	}
}
@include Book();
.box-out {
	width: 100%;
	padding-top: 1rem;
	position: static;
	display: flex;
	flex-wrap: wrap;
	.mystory-book:nth-child(2n + 1) {
		width: 50%;
		padding: 0 0 0 1rem;
	}
	.mystory-book:nth-child(2n) {
		padding: 0 1rem 0 0;
	}
}
</style>
