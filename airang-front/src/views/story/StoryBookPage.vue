<template>
	<section class="mystory-wrap">
		<div class="mystory-bookcover">
			<section class="mystory-page">
				<div class="mystory-face mystory-cover">
					<img v-if="cover" class="mystory-cover__img" :src="coverSrc" alt="" />
				</div>
				<div class="mystory-face mystory-inputbox"></div>
			</section>
			<section class="mystory-page mystory-bookpage">
				<div class="mystory-face mystory-books">
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
import { createMyStory, fetchMyStories, fetchStory } from '@/api/story';
export default {
	created() {
		this.fetchStoryBook();
		this.fetchBooks();
	},
	props: {
		storyId: Number,
	},
	data() {
		return {
			books: [],
			cover: null,
		};
	},
	computed: {
		imgSrc() {
			return process.env.VUE_APP_API_URL;
		},
		coverSrc() {
			return `${process.env.VUE_APP_API_URL}${this.filterMedia(this.cover)}`;
		},
	},
	watch: {
		$route() {
			this.fetchBooks();
		},
	},
	mounted() {
		const page = document.querySelectorAll('.mystory-page');
		setTimeout(function() {
			page[0].classList.add('flipped');
		}, 1000);
	},
	methods: {
		async fetchStoryBook() {
			try {
				const { data } = await fetchStory(this.storyId);
				console.log(data);
				this.cover = data.cover_image;
			} catch (error) {
				console.log(error);
			}
		},
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
	position: relative;
	width: 100%;
	min-height: 100vh;
	.mystory-bookcover {
		position: absolute;
		left: 0;
		right: 0;
		top: 0;
		bottom: 0;
		width: 80vw;
		height: 90vh;
		transform-style: preserve-3d;
		margin: auto;
		.mystory-face:nth-child(2) {
			transform: rotateY(180deg);
		}
		.mystory-page {
			position: absolute;
			left: 50%;
			top: 0;
			width: 50%;
			height: 100%;
			transform-style: preserve-3d;
			transition: 1.5s;
			box-shadow: 0 2px 6px 0 rgba(68, 67, 68, 0.5);

			&:nth-child(1) {
				z-index: 2;
				transform-origin: left;
			}
			&:nth-child(2) {
				z-index: 1;
			}
			&:nth-child(1).flipped {
				transform: rotateY(-180deg);
			}
			.mystory-face {
				position: absolute;
				left: 0;
				top: 0;
				width: 100%;
				height: 100%;
				background: rgba(#fff8dc, 0.8);
				backface-visibility: hidden;
			}
			.mystory-books {
				width: 100%;
				height: 100%;
				display: flex;
				flex-wrap: wrap;
				.mystory-book {
					width: 50%;
					display: flex;
					justify-content: center;
					align-items: center;
					margin: 0;
				}
			}
			.mystory-inputbox {
				display: flex;
				flex-direction: column;
				justify-content: center;
				align-items: center;
			}
		}
	}
}
@-webkit-keyframes bookBlock {
	from {
		transform: rotateY(180deg);
	}
	to {
		transform: rotateY(-180deg);
	}
}
.mystory-cover {
	width: 100%;
	display: flex;
	justify-content: center;
	align-items: center;
	.mystory-cover__img {
		width: 100%;
		height: 100%;
		object-fit: fill;
	}
}
@include Book();
</style>
