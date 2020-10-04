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
			<section class="story-left">
				<div class="story-left-box">
					<img
						class="story-left__bg"
						:src="`${imgSrc}${filterMedia(story.back_image)}`"
						alt=""
					/>
					<!-- eslint-disable vue/no-use-v-if-with-v-for,vue/no-confusing-v-for-v-if -->
					<img
						:key="image.id"
						v-for="image in story.images"
						v-if="image.order === scriptNumber + 1 && !image.is_main_character"
						:src="`${imgSrc}${filterMedia(image.path)}`"
						:class="[
							`story-left__character`,
							`order${image.order}`,
							`sub${story.id}-${image.id}`,
						]"
						alt=""
					/>
					<img
						:key="image.id"
						v-for="image in story.images"
						v-if="image.order === scriptNumber + 1 && image.is_main_character"
						:src="`${imgSrc}images/user/${userId}/mystory/${myStoryId}/0.png`"
						:class="[
							`story-left__character`,
							`order${image.order}`,
							`sub${story.id}-${image.id}`,
						]"
						alt=""
					/>
					<img
						v-if="job"
						:class="[`story-left__character`, `job-${job}`]"
						:src="
							`${imgSrc}images/user/${userId}/mystory/${myStoryId}/${job}.png`
						"
						alt=""
					/>
				</div>
			</section>
			<StoryFinishItem
				@page-decrease="currentDecrease"
				@page-increase="currentIncrease"
				:scripts="story.scripts"
				:subId="story.id"
				:userId="userId"
			/>
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
		BaseURL() {
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
			userId: null,
			nextStoryId: null,
			finish: false,
			coverImage: null,
			bookName: null,
			leftBox: [],
			job: 0,
		};
	},
	destroyed() {
		this.currentItem = -1;
		this.scriptNumber = 0;
		this.stories = [];
		this.startStory = null;
		this.nextStoryId = null;
		this.finish = false;
		this.coverImage = null;
		this.bookName = null;
		this.job = 0;
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
				this.coverImage = data.story.cover_image;
				this.bookName = data.story.name;
				this.nextStoryId = data.mystory.next_id;
				this.startStory = data.mystory.substory;
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
							switch (data.substory.id) {
								case 47:
									this.job = 4;
									break;
								case 46:
									this.job = 5;
									break;
								case 45:
									this.job = 2;
									break;
								case 44:
									this.job = 1;
									break;
								case 43:
									this.job = 3;
									break;
								default:
									this.job = 0;
							}
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
			this.stories.push(this.startStory);

			this.currentItem = 0;
		},
		nextPage() {
			this.currentItem += 1;
		},
		exitStory() {
			this.$router.push({ name: 'bookshelf' });
		},
	},
	beforeUpdate() {
		const playingSounds = document.querySelectorAll('.story-sound__playing');
		if (playingSounds) {
			playingSounds.forEach(playingSound => {
				playingSound.pause();
			});
		}
	},
	mounted() {
		const id = this.$store.getters.getId;
		this.userId = parseInt(id);
		bus.$on('finished:page-increase', this.currentIncrease);
		bus.$on('finished:script-increase', this.scriptIncrease);
		bus.$on('finished:script-reset', this.resetScript);
		bus.$on('finished:next-page', this.updateStory);
		this.createStory(this.myStoryId);
	},
};
</script>

<style lang="scss">
@import '@/assets/scss/test/_hwang.scss';
@import '@/assets/scss/test/_kim.scss';
@import '@/assets/scss/test/_hong.scss';
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
		width: 50%;
		height: 100%;
		box-shadow: 0 2px 6px 0 rgba(68, 67, 68, 0.4);
		display: flex;
		justify-content: center;
		align-items: center;
		.story-left-box {
			position: relative;
		}
		.story-left__character {
			z-index: 2;
			position: absolute;
			transform: translate(-50%, 50%);
		}
		.story-left__bg {
			z-index: 1;
			width: 100%;
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
