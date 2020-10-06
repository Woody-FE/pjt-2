<template>
	<section class="profileStory-wrap">
		<header class="profileStory-header">
			<p class="profileStory-header__name">
				나의 책장
			</p>
		</header>
		<section class="profileShelf-wrap__background">
			<img
				src="@/assets/images/bookShelf/bookshelf.png"
				class="bookshelf-bg"
				alt="bookshelf"
			/>
			<span class="bookshelf-bg2"></span>
			<span class="bookshelf-bg2 bookshelf-bg3"></span>
			<img
				src="@/assets/images/bookShelf/library_arang.png"
				class="bookshelf-arang"
				alt="bookshelf-arang"
			/>
		</section>
		<section class="profileStory-select"></section>
		<div class="bookshelf">
			<div class="first-bookshelf-books">
				<div class="bookshelf-book" :key="book.id" v-for="book in firstBooks">
					<figure class="book-items">
						<ProfileBook :book="book"></ProfileBook>
					</figure>
				</div>
			</div>
		</div>
		<div class="bookshelf">
			<div class="second-bookshelf-books">
				<div class="bookshelf-book" :key="book.id" v-for="book in secondBooks">
					<figure class="book-items">
						<ProfileBook :book="book"></ProfileBook>
					</figure>
				</div>
			</div>
		</div>
	</section>
</template>

<script>
import bus from '@/utils/bus';
import { fetchMyStories } from '@/api/story';
import { truncateString } from '@/utils/validation';
import ProfileBook from '@/components/profile/ProfileBook.vue';
export default {
	components: {
		ProfileBook,
	},
	props: {
		userName: Number,
	},
	data() {
		return {
			firstBooks: [],
			secondBooks: [],
			whatBook: 'all',
		};
	},
	computed: {
		baseURL() {
			return process.env.VUE_APP_API_URL;
		},
	},
	methods: {
		async fetchBooks() {
			try {
				const { data } = await fetchMyStories();
				this.firstBooks = data.slice(0, 3);
				this.secondBooks = data.slice(3, 6);
				this.firstBooks.forEach(el => {
					el.story_name = truncateString(el.story_name);
				});
				this.secondBooks.forEach(el => {
					el.story_name = truncateString(el.story_name);
				});
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
		changeStatus() {
			return;
		},
	},
	created() {
		bus.$on('clearDelete', this.fetchBooks);
		this.fetchBooks();
	},
};
</script>

<style lang="scss">
.profileStory-wrap {
	width: 100%;
	height: 100%;
	display: flex;
	flex-direction: column;
	position: relative;
	.profileStory-header {
		margin-bottom: 1rem;
		display: flex;
		align-content: content;
		border-left: 3px solid #c27129;
		padding-left: 5px;
		// .profileStory-header__span {
		// 	display: inline-block;
		// 	width: 3px;
		// 	height: 1.5rem;
		// 	background: yellow;
		// 	margin-right: 5px;
		// }
		.profileStory-header__name {
			font-size: 1.5rem;
		}
	}
}
.profileStory-footer {
	margin-bottom: 10rem;
}

// bookshelf-bg
.profileShelf-wrap__background {
	height: 700px;
	perspective: 700px;
	.bookshelf-bg {
		width: 100%;
		height: 650px;
		position: absolute;
		top: 50px;
	}
	.bookshelf-bg2 {
		width: 80%;
		height: 60px;
		position: absolute;
		top: 300px;
		left: 50%;
		border-radius: 50px;
		border-bottom: 5px solid rgb(99, 58, 23);
		background: linear-gradient(
			rgba(99, 58, 23, 0.5) 3%,
			rgb(194, 113, 41),
			rgb(226, 136, 57)
		);
		transform: translateX(-50%) rotateX(35deg);
		box-shadow: 0px 10px 5px rgba(99, 58, 23, 0.5);
	}
	.bookshelf-bg3 {
		transform: translateX(-50%) rotateX(60deg);
		position: absolute;
		top: 600px;
		left: 50%;
	}
	.bookshelf-arang {
		width: 200px;
		position: absolute;
		bottom: 100px;
		right: -150px;
		animation: leftRight 1.5s ease-in-out infinite;
		z-index: 9999;
	}
}
.first-bookshelf-books {
	width: 100%;
	height: 100%;
	display: flex;
	flex-wrap: wrap;
	padding-left: 7%;
	.bookshelf-book {
		width: 24%;
		display: flex;
		justify-content: center;
		align-items: center;
		margin: 1rem 0;
		.book-items {
			width: 14%;
			height: 200px;
			position: absolute;
			bottom: 53%;
			@media screen and (max-width: 1024px) {
				height: 180px;
			}
			@media screen and (max-width: 768px) {
				height: 160px;
			}
		}
	}
}
.second-bookshelf-books {
	// position: absolute;
	// top: 650px;
	width: 100%;
	display: flex;
	flex-wrap: wrap;
	padding-left: 7%;
	.bookshelf-book {
		width: 24%;
		display: flex;
		justify-content: center;
		align-items: center;
		margin: 1rem 0;
		.book-items {
			position: absolute;
			width: 14%;
			height: 200px;
			position: absolute;
			bottom: 18%;
			@media screen and (max-width: 1024px) {
				height: 180px;
			}
			@media screen and (max-width: 768px) {
				height: 160px;
			}
		}
	}
}
</style>
