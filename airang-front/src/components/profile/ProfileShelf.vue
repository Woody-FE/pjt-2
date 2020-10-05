<template>
	<section class="profileStory-wrap">
		<header class="profileStory-header">
			<span class="profileStory-header__span"></span>
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
			<section></section>
		</section>
		<section class="profileStory-select"></section>
		<div class="bookshelf">
			<div class="first-bookshelf-books">
				<div class="bookshelf-book" :key="book.id" v-for="book in firstBooks">
					<router-link :to="`/story/${book.story.id}/review/${book.id}`">
						<img
							src="@/assets/images/default_book.jpg"
							class="book-pace"
							alt="book-pace"
						/>
						<span class="book-name">{{ book.story_name }}</span>
					</router-link>
				</div>
			</div>
		</div>
		<div class="bookshelf">
			<div class="second-bookshelf-books">
				<div class="bookshelf-book" :key="book.id" v-for="book in secondBooks">
					<router-link :to="`/bookshelf/${book.id}`">
						<img
							src="@/assets/images/default_book.jpg"
							class="book-pace"
							alt="book-pace"
						/>
						<span class="book-name">{{ book.story_name }}</span>
					</router-link>
				</div>
			</div>
		</div>
	</section>
</template>

<script>
import { fetchMyStories } from '@/api/story';
import { truncateString } from '@/utils/validation';

export default {
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
				console.log(data);
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
		margin-bottom: 1.5rem;
		display: flex;
		align-content: content;
		.profileStory-header__span {
			display: inline-block;
			width: 3px;
			height: 2rem;
			background: yellow;
			margin-right: 5px;
		}
		.profileStory-header__name {
			font-size: 2rem;
		}
	}
	.profileStory-footer {
	}
}
.box-out {
	z-index: 10;
	width: 720px;
	display: flex;
	// justify-content: space-between;
	align-items: center;
	// position: absolute;
	// top: 140px;
}

.book {
	width: 180px;
	height: 255px;
	margin-right: 30px;
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
	// background: url('data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAD8AAABhCAYAAABh23lYAAAACXBIWXMAAAsTAAALEwEAmpwYAAAAAXNSR0IArs4c6QAAAARnQU1BAACxjwv8YQUAAAHCSURBVHgB7dxPTsJAHMXxN7Xu3UhigobxJHACvQFwAr2BcgO8AZxE7uGiDZiQyEIW7oSOUyKbKgLS8u+9b9JNF818fum0XdWUhy9VEDZBGIdBGD6DsFM3bQYgTnjWhGdNeNaEZ0141oRnTXjWhGdNeNaEZ0141oRnTXjWhGdNeNaEZ0141oRnTXjWhGdNeNaEZ0141oRnTXjWhGdNeNaEZ0141oRnTXjWhGdNeNaEZ0141oRnTXjWhGdNeNZ2hR/7o+UcmnCIsaNCbLcU/RR8oB1bO/4+17l8ixoGeIBBBVvMXI0ih+L7Df2j8iiqnvgh+AVVUXDOTZvF4tNb2qC7DJ1tNgSDO78tblFQxeE92l+0NSjZDjaoMowqyYl7hDF15JzL+x+YHtxLgFq/ZO2m8LT4wsb90nUjmMD61XaRc7ng5+jBua29ntsecq6oIWyELxqdLe8h/GvPp+h0T28D/FezZ8Ip7pHgZt3X5NoPvH1BZ5sNIUTDL7C+6hBWxxt0gk+00tsOe96qH0zL8GO4pBtMg/YhoLMtG8Ii/EpfY4fSoiFk8UeFzpYdwhz/jiNGZ0uHEBjUEzftohJFZyAsdX8BM0/amLC3spYAAAAASUVORK5CYII=');
	background-size: 16px;
	background-repeat: no-repeat;
}

/*------ background-pic ------*/

.books-1 {
	background: url('https://search.pstatic.net/common/?src=http%3A%2F%2Fblogfiles.naver.net%2F20140716_200%2F500farm_1405513399454S2F1z_PNG%2F%25B5%25BF%25C8%25AD%25C3%25A51%25B8%25E9.png&type=sc960_832');
	background-size: 180px 255px;
}

.books-2 {
	background: url('https://search.pstatic.net/common/?src=http%3A%2F%2Fblogfiles.naver.net%2F20140716_200%2F500farm_1405513399454S2F1z_PNG%2F%25B5%25BF%25C8%25AD%25C3%25A51%25B8%25E9.png&type=sc960_832');
	background-size: 180px 255px;
}

.books-3 {
	background: url('https://upload-images.jianshu.io/upload_images/3433202-564e196e8b409f16.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240');
	background-size: 180px 255px;
}

/* ----- hover ----- */

.book:hover {
	cursor: pointer;
	transform: rotateY(-28deg) rotateZ(-2deg) scale(1.02);
	-webkit-backface-visibility: hidden;
	box-shadow: 1px 3px 2px #353d85, 20px 8px 0 #525dc4;
	/* transform: scale(1.02); */
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
.profileStory-footer {
	margin-bottom: 10rem;
}

// bookshelf-bg
.profileShelf-wrap__background {
	height: 700px;
	.bookshelf-bg {
		width: 100%;
		height: 650px;
		position: absolute;
		top: 50px;
	}
	.bookshelf-bg2 {
		width: 80%;
		height: 50px;
		position: absolute;
		top: 300px;
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
		position: absolute;
		top: 600px;
		left: 50%;
	}
	.bookshelf-arang {
		width: 200px;
		position: absolute;
		bottom: 200px;
		right: -50px;
		animation: leftRight 1.5s ease-in-out infinite;
	}
}
.first-bookshelf-books {
	width: 100%;
	height: 100%;
	display: flex;
	flex-wrap: wrap;
	.bookshelf-book {
		width: 26%;
		display: flex;
		justify-content: center;
		align-items: center;
		margin: 1rem 0;
		.book-name {
			position: absolute;
			font-size: 1.5rem;
			top: 90px;
			margin-left: 27px;
			color: black;
		}
		.book-pace {
			width: 200px;
			height: 250px;
			position: absolute;
			top: 70px;
		}
	}
}
.second-bookshelf-books {
	position: absolute;
	top: 650px;
	width: 100%;
	display: flex;
	flex-wrap: wrap;
	.bookshelf-book {
		width: 26%;
		display: flex;
		justify-content: center;
		align-items: center;
		margin: 1rem 0;
		.book-name {
			position: absolute;
			font-size: 1.5rem;
			top: -250px;
			margin-left: 27px;
			color: black;
		}
		.book-pace {
			width: 200px;
			height: 240px;
			position: absolute;
			top: -270px;
		}
	}
}
</style>
