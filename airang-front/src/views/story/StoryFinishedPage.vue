<template>
	<section class="story-wrap">
		<article v-if="currentItem === -1" class="story-page story-current">
			<section class="story-main story-cover">
				<img
					class="story-cover__img"
					v-if="this.coverImage"
					:src="`${imgSrc}${filterMedia(this.coverImage)}`"
					:alt="`${this.bookName}`"
				/>
			</section>
			<section class="story-start">
				<button @click="startPage" class="story-start-btn">
					시작하기
				</button>
			</section>
		</article>
		<article
			:data-index="index"
			:key="index"
			v-for="(story, index) in stories"
			class="story-page hidden"
			:class="[currentItem === index ? 'story-abled' : 'story-disabled']"
		>
			<section v-if="!story.question" class="story-left">
				<div class="story-left-box">
					<img
						class="story-left__bg"
						:src="`${imgSrc}${filterMedia(story.back_image)}`"
						alt=""
					/>
					<img
						class="story-left__user1"
						v-if="currentItem === 1"
						src="@/assets/images/user/baby_default.png"
						alt=""
					/>
					<img
						v-if="story.id === 4"
						class="story-left__user2"
						src="@/assets/images/user/baby_default.png"
						alt=""
					/>
				</div>
			</section>
			<section v-else class="story-left story-select">
				<button
					class="story-select__btn"
					@click="createSubStory(story.selects[0].substory)"
				>
					{{ story.selects[0].select }}
				</button>
			</section>
			<StoryFinishItem
				v-if="!story.question"
				@page-decrease="currentDecrease"
				@page-increase="currentIncrease"
				:scripts="story.scripts"
				:subId="story.id"
			/>
			<section v-else class="story-right story-select">
				<button
					class="story-select__btn"
					@click="createSubStory(story.selects[1].substory)"
				>
					{{ story.selects[1].select }}
				</button>
			</section>
		</article>
		<section class="story-delete__btn">
			<button @click="exitStory" class="story-delete-btn">
				<i class="icon ion-md-close"></i>
			</button>
		</section>
	</section>
</template>

<script>
import bus from '@/utils/bus';
import StoryFinishItem from '@/components/story/StoryFinishItem.vue';
import { fetchMyStory, fetchMySubStory } from '@/api/story';
export default {
	components: {
		StoryFinishItem,
	},
	props: {
		storyId: Number,
		myStoryId: Number,
	},
	computed: {
		imgSrc() {
			return process.env.VUE_APP_API_URL;
		},
		userSrc() {
			return '@/assets/images/user/baby_default.png';
		},
	},
	data() {
		return {
			currentItem: -1,
			scriptNumber: 0,
			stories: [],
			nextStoryId: null,
			finish: false,
			coverImage: null,
			bookName: null,
		};
	},
	destroyed() {
		this.currentItem = -1;
		this.scriptNumber = 0;
		this.stories = [];
		this.nextStoryId = null;
		this.finish = false;
		this.coverImage = null;
		this.bookName = null;
	},
	methods: {
		resetScript() {
			this.scriptNumber = 0;
		},
		currentIncrease() {
			this.currentItem += 1;
		},
		currentDecrease() {
			this.currentItem -= 1;
		},
		scriptDecrease() {
			this.scriptNumber -= 1;
		},
		scriptIncrease() {
			this.scriptNumber += 1;
		},
		async createStory(mystoryId) {
			try {
				const { data } = await fetchMyStory(mystoryId);
				console.log(data);
				this.coverImage = data.story.cover_image;
				this.bookName = data.story.name;
				this.nextStoryId = data.mystory.next_id;
				this.stories.push(data.mystory.substory);
			} catch (error) {
				console.log(error);
			}
		},
		async updateStory() {
			try {
				if (this.finish) {
					this.$router.push({ name: 'bookshelf' });
				} else {
					if (this.nextStoryId) {
						const { data } = await fetchMySubStory(
							this.myStoryId,
							this.nextStoryId,
						);
						if (data.next_id === null) {
							this.finish = true;
						}
						this.nextStoryId = data.next_id;
						this.stories.push(data.substory);
					}
				}
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
		startPage() {
			const startBtn = document.querySelector('.story-start-btn');
			startBtn.style.display = 'none';
			const storyCover = document.querySelectorAll('.story-page');
			setTimeout(function() {
				storyCover[0].classList.add('story-disabled');
			}, 500);
			this.currentItem = 0;
		},
		nextPage() {
			this.currentItem += 1;
		},
		exitStory() {
			this.$router.push({ name: 'bookshelf' });
		},
	},
	mounted() {
		bus.$on('finished:page-increase', this.currentIncrease);
		bus.$on('finished:script-increase', this.scriptIncrease);
		bus.$on('finished:script-reset', this.resetScript);
		bus.$on('finished:next-page', this.updateStory);
		this.createStory(this.myStoryId);
	},
};
</script>

<style lang="scss">
.story-wrap {
	width: 100%;
	height: 100vh;
	position: relative;
	perspective: 1000px;
	.story-start {
		position: absolute;
		bottom: 2rem;
		left: 50%;
		width: 10rem;
		height: 4rem;
		transform: translateX(-50%);
		.story-start-btn {
			border: none;
			border-radius: 8px;
			width: 10rem;
			height: 4rem;
			font-size: 1.5rem;
			background: black;
			color: white;
			cursor: pointer;
		}
	}
}
.story-delete__btn {
	position: absolute;
	top: 3rem;
	right: 3rem;
	width: 3rem;
	height: 3rem;
	/* transform: translateX(-50%); */
	.story-delete-btn {
		border: none;
		border-radius: 50%;
		width: 3rem;
		height: 3rem;
		font-size: 1.5rem;
		background: white;
		color: black;
		cursor: pointer;
	}
}
.story-disabled {
	/* opacity: 0;
    position: absolute;
    top: -100vh;
    left: -100vw; */
	animation: fade-out 1s;
	animation-fill-mode: forwards;
}

.story-page {
	width: 100%;
	height: 100vh;
	display: flex;
	flex-wrap: wrap;
	transition: 1s;
	.story-left {
		/* position: relative; */
		width: 50%;
		height: 100%;
		box-shadow: 0 2px 6px 0 rgba(68, 67, 68, 0.4);
		display: flex;
		justify-content: center;
		align-items: center;
		.story-left-box {
			position: relative;
		}
		.story-left__bg {
			z-index: 1;
		}
		.story-left__user1 {
			z-index: 2;
			position: absolute;
			width: 50%;
			bottom: 29%;
			left: 47%;
			transform: translateX(-50%);
		}
		.story-left__user2 {
			z-index: 2;
			position: absolute;
			width: 50%;
			bottom: 29%;
			left: 35%;
			transform: rotatetranslateX(-50%);
		}
	}
	.story-right {
		width: 50%;
		height: 100%;
		box-shadow: 0 2px 6px 0 rgba(68, 67, 68, 0.4);
		display: flex;
		flex-direction: column;
		justify-content: center;
		align-items: center;
	}
	.story-select {
		position: relative;
		display: flex;
		justify-content: center;
		align-items: center;
	}
	.story-main {
		width: 100%;
		height: 100%;
		box-shadow: 0px 2px 6px rgba(0, 0, 0, 0.4);
	}
	.stroy-main::before {
		background: linear-gradient(
			to right,
			rgba(0, 0, 0, 0.2) 0px,
			transparent 5%,
			transparent 95%,
			rgba(0, 0, 0, 0.2) 100%
		);
	}
	.story-cover {
		display: flex;
		justify-content: center;
		align-items: center;
		.story-cover__img {
			height: 100%;
			object-fit: cover;
		}
	}
	.story-select__btn {
		position: absolute;
		top: 50%;
		left: 50%;
		transform: translate(-50%, 50%);
		background: black;
		color: white;
		border: none;
		width: 300px;
		height: 50px;
		font-size: 1rem;
		border-radius: 8px;
		cursor: pointer;
	}
}
.story-abled {
	/* opacity: 1;
    position: static; */
	animation: fade-in 1s;
	animation-fill-mode: forwards;
	display: flex !important;
}

.hidden {
	display: none;
	opacity: 0;
}

@keyframes fade-in {
	from {
		opacity: 0;
	}
	to {
		opacity: 1;
	}
}

@keyframes fade-out {
	from {
		opacity: 1;
	}
	to {
		opacity: 0;
	}
}
</style>
