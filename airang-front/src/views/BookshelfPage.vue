<template>
	<section class="bookshelf-wrap">
		<h2>아이랑 도서관</h2>
		<div class="box-out">
			<router-link
				:key="book.id"
				v-for="book in books"
				:to="`/story/${book.id}/${book.story.substory}`"
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
					await createMyStory({
						story_id: 1,
						story_name: '세가지 선물',
					});
					this.fetchBooks();
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

.box-out {
	z-index: 10;
	width: 100%;
	display: flex;
	flex-wrap: wrap;
	/* margin: 0 -1rem; */
	/* justify-content: space-between; */
	/* align-items: center; */
	position: absolute;
	top: 140px;
}

.book {
	width: 180px;
	height: 255px;
	/* flex: 1 1 auto; */
	/* padding: 0 1rem; */
	/* margin: 0 1rem; */
	background-color: rgb(62, 71, 152);
	transition: all 0.3s ease-in-out;
	transform-origin: left center 0px;
	transform-style: preserve-3d;
	border-top-right-radius: 5px;
	border-bottom-right-radius: 5px;
	-webkit-backface-visibility: hidden;
	overflow: hidden;
}

.box-out .book::after {
	content: ' ';
	display: block;
	opacity: 0;
	width: 180px;
	height: 255px;
	position: relative;
	left: 8px;
	transition: all 0.3s ease;
}

.box-out .book::before {
	content: ' ';
	z-index: 999;
	display: block;
	width: 20px;
	height: 100px;
	opacity: 0;
	position: absolute;
	top: -12px;
	right: 8px;
	transition: all 0.25s;
	background: url('data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAD8AAABhCAYAAABh23lYAAAACXBIWXMAAAsTAAALEwEAmpwYAAAAAXNSR0IArs4c6QAAAARnQU1BAACxjwv8YQUAAAHCSURBVHgB7dxPTsJAHMXxN7Xu3UhigobxJHACvQFwAr2BcgO8AZxE7uGiDZiQyEIW7oSOUyKbKgLS8u+9b9JNF818fum0XdWUhy9VEDZBGIdBGD6DsFM3bQYgTnjWhGdNeNaEZ0141oRnTXjWhGdNeNaEZ0141oRnTXjWhGdNeNaEZ0141oRnTXjWhGdNeNaEZ0141oRnTXjWhGdNeNaEZ0141oRnTXjWhGdNeNaEZ0141oRnTXjWhGdNeNZ2hR/7o+UcmnCIsaNCbLcU/RR8oB1bO/4+17l8ixoGeIBBBVvMXI0ih+L7Df2j8iiqnvgh+AVVUXDOTZvF4tNb2qC7DJ1tNgSDO78tblFQxeE92l+0NSjZDjaoMowqyYl7hDF15JzL+x+YHtxLgFq/ZO2m8LT4wsb90nUjmMD61XaRc7ng5+jBua29ntsecq6oIWyELxqdLe8h/GvPp+h0T28D/FezZ8Ip7pHgZt3X5NoPvH1BZ5sNIUTDL7C+6hBWxxt0gk+00tsOe96qH0zL8GO4pBtMg/YhoLMtG8Ii/EpfY4fSoiFk8UeFzpYdwhz/jiNGZ0uHEBjUEzftohJFZyAsdX8BM0/amLC3spYAAAAASUVORK5CYII=');
	background-size: 16px;
	background-repeat: no-repeat;
}

/*------ background-pic ------*/

.books-1 {
	background: url('https://search.pstatic.net/common/?src=http%3A%2F%2Fblogfiles.naver.net%2F20140716_200%2F500farm_1405513399454S2F1z_PNG%2F%25B5%25BF%25C8%25AD%25C3%25A51%25B8%25E9.png&type=sc960_832');
	background-size: 100% 255px;
}

/* ----- hover ----- */

.book:hover {
	cursor: pointer;
	transform: rotateY(-28deg) rotateZ(-2deg) scale(1.02);
	-webkit-backface-visibility: hidden;
	box-shadow: 1px 3px 2px #353d85, 20px 8px 0 #525dc4;
}

.book:hover::after {
	content: ' ';
	display: block;
	opacity: 1;
	width: 172px;
	height: 255px;
	position: relative;
	left: 8px;
	background: linear-gradient(
		-180deg,
		rgba(255, 255, 255, 0.1) 0%,
		rgba(255, 255, 255, 0) 60%
	);
}

.book:hover::before {
	transform: translateY(9px);
	opacity: 1;
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
