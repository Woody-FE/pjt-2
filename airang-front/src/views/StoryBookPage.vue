<template>
	<section class="story-wrap">
		<article v-if="currentItem === -1" class="story-page story-current">
			<section class="story-main story-cover">
				왼쪽
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
				<img :src="`${imgSrc}${filterMedia(story.back_image)}`" alt="" />
			</section>
			<section v-else class="story-left story-select">
				<button
					class="story-select__btn"
					@click="createSubStory(story.selects[0].substory)"
				>
					{{ story.selects[0].select }}
				</button>
			</section>
			<StoryItem
				v-if="!story.question"
				@page-decrease="currentDecrease"
				@page-increase="currentIncrease"
				:scripts="story.scripts"
			/>
			<section v-else class="story-right">
				<button
					class="story-select__btn"
					@click="createSubStory(story.selects[1].substory)"
				>
					{{ story.selects[1].select }}
				</button>
			</section>
		</article>
		<!-- <article class="story-page story-finish">
            끝
        </article> -->
		<!-- <section class="story-btn">
            <button @click="nextPage" class="story-right-btn">
                <i class="icon ion-md-arrow-round-forward"></i>
            </button>
        </section> -->
	</section>
</template>

<script>
import bus from '@/utils/bus';
import StoryItem from '@/components/story/StoryItem.vue';
import { fetchSubStory, fetchBranch } from '@/api/story';
// import { finishedMyStory } from '@/api/story';
export default {
	components: {
		StoryItem,
	},
	props: {
		myStoryId: Number,
		subStoryId: Number,
	},
	computed: {
		imgSrc() {
			return process.env.VUE_APP_API_URL;
		},
	},
	data() {
		return {
			currentItem: -1,
			scriptNumber: 0,
			stories: [],
			nextStoryId: null,
			nextBranchId: null,
			hasBranch: null,
			finish: false,
			selectStories: [],
		};
	},
	created() {
		console.log('크리에이티드');
		this.currentItem = -1;
		this.scriptNumber = 0;
		this.stories = [];
		this.nextStoryId = null;
		this.nextBranchId = null;
		this.hasBranch = null;
		this.finish = false;
		this.selectStories = [];
	},
	destroyed() {
		console.log('디스트로이');
		this.currentItem = -1;
		this.scriptNumber = 0;
		this.stories = [];
		this.nextStoryId = null;
		this.nextBranchId = null;
		this.hasBranch = null;
		this.finish = false;
		this.selectStories = [];
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
		async createSubStory(num) {
			try {
				this.selectStories.push(num);
				const { data } = await fetchSubStory({
					mystory_id: this.myStoryId,
					substory_id: num,
				});
				console.log(data.next_id);
				console.log(this.stories);

				this.hasBranch = data.has_branch;
				console.log(this.hasBranch);
				if (!this.hasBranch) {
					this.nextStoryId = data.next_id;
					this.nextBranchId = 0;
				} else {
					this.nextBranchId = data.next_id;
					this.nextStoryId = 0;
				}
				this.stories.push(data);
				if (this.currentItem !== -1) {
					this.currentItem += 1;
				}
			} catch (error) {
				console.log(error);
			}
		},
		async updateStory() {
			try {
				if (this.finish) {
					console.log('끝', this.nextStoryId);
					// await finishedMyStory(this.myStoryId, this.selectStories);
					this.$router.push({ name: 'bookshelf' });
				} else {
					if (this.nextStoryId) {
						this.selectStories.push(this.nextStoryId);
						const { data } = await fetchSubStory({
							mystory_id: this.myStoryId,
							substory_id: this.nextStoryId,
						});
						console.log(data.next_id);
						console.log(this.stories);
						if (data.next_id === -1) {
							this.finish = true;
						}
						this.hasBranch = data.has_branch;
						if (!this.hasBranch) {
							this.nextStoryId = data.next_id;
							this.nextBranchId = 0;
						} else {
							this.nextBranchId = data.next_id;
							this.nextStoryId = 0;
						}
						this.stories.push(data);
					} else if (this.nextBranchId) {
						const { data } = await fetchBranch(this.nextBranchId);
						console.log(data);
						this.stories.push(data);
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
	},
	mounted() {
		console.log('마운티드');
		bus.$on('page-increase', this.currentIncrease);
		// bus.$on('page-decrease', this.currentDecrease);
		bus.$on('script-increase', this.scriptIncrease);
		// bus.$on('script-decrease', this.scriptDecrease);
		bus.$on('script-reset', this.resetScript);
		bus.$on('next-page', this.updateStory);
		this.createSubStory(this.subStoryId);
	},
	watch: {
		$route() {
			console.log('왓치드');
			this.currentItem = -1;
			this.scriptNumber = 0;
			this.stories = [];
			this.nextStoryId = 0;
			this.nextBranchId = null;
			this.hasBranch = null;
			this.finish = false;
			this.selectStories = [];
			this.createSubStory(this.subStoryId);
		},
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
		width: 4rem;
		height: 4rem;
		transform: translateX(-50%);
		.story-start-btn {
			border: none;
			border-radius: 50%;
			width: 4rem;
			height: 4rem;
			font-size: 0.5rem;
			background: black;
			color: white;
			cursor: pointer;
		}
	}
}
.story-btn {
	position: absolute;
	bottom: 2rem;
	left: 50%;
	width: 3rem;
	height: 3rem;
	transform: translateX(-50%);
	.story-right-btn {
		border: none;
		border-radius: 50%;
		width: 3rem;
		height: 3rem;
		font-size: 1.5rem;
		background: black;
		color: white;
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
		width: 50%;
		height: 100%;
		box-shadow: 0 2px 6px 0 rgba(68, 67, 68, 0.4);
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
	}
	.story-select__btn {
		background: black;
		color: white;
		border: none;
		width: 300px;
		height: 50px;
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
