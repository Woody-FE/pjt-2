<template>
	<section class="bookshelf-wrap">
		<h2>아이랑 도서관</h2>
		<img
			src="@/assets/images/bookShelf/bookshelf.png"
			class="bookshelf-bg"
			alt="bookshelf"
		/>
		<!-- <span class="bookshelf-bg2"></span> -->
		<span class="bookshelf-bg2 bookshelf-bg3"></span>
		<img
			src="@/assets/images/bookShelf/shelf.png"
			class="bookshelf-shelf"
			alt="bookshelf-shelf"
		/>
		<img
			src="@/assets/images/bookShelf/library_arang.png"
			class="bookshelf-arang"
			alt="bookshelf-arang"
		/>
		<div class="bookshelf">
			<div class="bookshelf-books">
				<div class="bookshelf-book" :key="book.id" v-for="book in books">
					<router-link :to="`/bookshelf/${book.id}`">
						<img
							:src="`${imgSrc}${filterMedia(book.cover_image)}`"
							class="book-pace"
							alt="book-pace"
						/>
					</router-link>
					<router-link :to="`/notservice`">
						<img
							src="@/assets/images/bookShelf/otherBook.jpg"
							class="book-pace book-pace2"
							alt="book-pace"
						/>
					</router-link>
					<router-link to="/myteam">
						<img
							src="@/assets/images/bookShelf/friendsBook.jpg"
							class="book-pace book-pace3"
							alt="book-pace"
						/>
					</router-link>
				</div>
			</div>
		</div>
	</section>
</template>

<script>
import { fetchStories } from '@/api/story';
import bus from '@/utils/bus';

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
			} catch (error) {
				bus.$emit('show:warning', '책을 가져오는데 실패했어요 :(');
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
	position: relative;
	perspective: 500px;
	h2 {
		font-size: 24px;
		border-left: 3px solid rgb(194, 113, 41);
		padding-left: 5px;
	}
}
.bookshelf-bg {
	width: 100%;
	height: 550px;
	position: absolute;
	top: 50px;
}
.bookshelf-bg2 {
	width: 80%;
	height: 50px;
	position: absolute;
	top: 180px;
	left: 50%;
	border-radius: 30px;
	border-bottom: 5px solid rgb(99, 58, 23);
	background: linear-gradient(
		rgba(99, 58, 23, 0.5) 3%,
		rgb(194, 113, 41),
		rgb(226, 136, 57)
	);
	transform: translateX(-50%) rotateX(55deg);
	box-shadow: 0px 10px 5px rgba(99, 58, 23, 0.5);
}
.bookshelf-bg3 {
	transform: translateX(-50%) rotateX(80deg);
	position: absolute;
	top: 360px;
	left: 50%;
}
.bookshelf-shelf {
	width: 28%;
	position: absolute;
	bottom: -500px;
	right: 210px;
	@media screen and (max-width: 768px) {
		width: 33%;
		bottom: -490px;
		right: 180px;
	}
}
.bookshelf-arang {
	width: 200px;
	position: absolute;
	bottom: -550px;
	right: -50px;
	animation: leftRight 1.5s ease-in-out infinite;
}
@keyframes leftRight {
	0% {
		transform: rotate(-2deg);
	}
	30% {
		transform: rotate(5deg);
	}
	60% {
		transform: rotate(3deg);
	}
	100% {
		transform: rotate(-2deg);
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
		.book-pace {
			width: 16%;
			position: absolute;
			bottom: -574%;
			&:hover {
				transform: rotate(5deg);
			}
			&:active {
				transform: scale(1.1) rotate(5deg);
			}
		}
		.book-pace2 {
			left: 42%;
		}
		.book-pace3 {
			left: 67%;
		}
	}
}
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
