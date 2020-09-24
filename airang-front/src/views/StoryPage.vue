<template>
	<div class="bb-custom-wrapper">
		<div id="bb-bookblock" class="bb-bookblock">
			<div class="bb-item after-select">
				<div class="bb-custom-firstpage">
					<img
						class="first-cover"
						src="@/assets/images/character/arang3.jpg"
						alt="img"
					/>
					<nav class="codrops-nav">
						<router-link to="/" class="codrops-icon codrops-icon-prev"
							><span>메인으로</span></router-link
						>
						<router-link to="/bookshelf" class="codrops-icon codrops-icon-prev"
							><span>책장으로</span></router-link
						>
					</nav>
				</div>
				<div class="bb-custom-side first-side">
					<p>
						세가지 선물
					</p>
				</div>
			</div>
			<div class="bb-item before-select">
				<div class="bb-custom-side img-side">
					<img src="@/assets/images/character/arang1.png" alt="img" />
					<img
						class="bb-img-character"
						src="https://j3d105.p.ssafy.io:8001/images/character/nukkied_girl.png"
						alt=""
					/>
				</div>
				<StoryTextItem v-if="stories.length" :scripts="stories[0].scripts" />
			</div>
			<div class="bb-item before-select">
				<div class="bb-custom-side img-side">
					<button class="btn btn-1" @click="firstChoice">
						여우
					</button>
				</div>
				<div class="bb-custom-side">
					<button class="btn btn-2" @click="secondChoice">토끼</button>
				</div>
			</div>
			<div class="bb-item before-select">
				<div class="bb-custom-side img-side">
					<img src="@/assets/images/character/arang1.png" alt="img" />
				</div>
				<StoryTextItem v-if="stories.length" :scripts="stories[1].scripts" />
			</div>
			<div class="bb-item before-select">
				<div class="bb-custom-side img-side">
					<img src="@/assets/images/character/arang1.png" alt="img" />
				</div>
				<StoryTextItem v-if="stories.length" :scripts="stories[2].scripts" />
			</div>
			<div class="bb-item before-select">
				<div class="bb-custom-side img-side">
					<img src="@/assets/images/character/arang1.png" alt="img" />
				</div>
				<StoryTextItem v-if="stories.length" :scripts="stories[3].scripts" />
			</div>
			<div class="bb-item before-select">
				<div class="bb-custom-side img-side">
					<img
						v-if="1 in status"
						src="@/assets/images/character/arang1.png"
						alt="img"
					/>
					<img v-else src="@/assets/images/character/arang1.png" alt="img" />
				</div>
				<!-- <div class="bb-custom-side">
					<div class="portrait-box">
						<img
							class="portrait-img"
							src="@/assets/images/character/arang1.png"
							alt=""
						/>
						<p class="portrait-p">나레이션</p>
					</div>
					<p v-if="2 in status">
						토끼는 나무둥지 앞에 멈춰섰어요<br />
						그런데! 갑자기 토끼의 크기가 개미같이 줄어들었어요
					</p>
					<p v-else-if="1 in status">
						여우는 할머니 모습으로 산을 내려갔어요.<br />그리고 혼례가 열리는
						잔칫집으로 쏙 들어갔어요!
					</p>
				</div> -->
				<StoryTextItem v-if="stories.length" :scripts="stories[4].scripts" />
			</div>
			<div class="bb-item">
				<div class="bb-custom-side img-side">
					<img
						v-if="1 in status"
						src="@/assets/images/character/arang1.png"
						alt="img"
					/>
					<img
						v-else-if="2 in status"
						src="@/assets/images/character/arang1.png"
						alt="img"
					/>
				</div>
				<div class="bb-custom-side">
					<div class="portrait-box">
						<img
							v-if="2 in status"
							class="portrait-img"
							src="@/assets/images/character/arang1.png"
							alt=""
						/>
						<img
							v-else-if="1 in status"
							class="portrait-img"
							src="@/assets/images/character/arang1.png"
							alt=""
						/>
						<p v-if="2 in status" class="portrait-p">영준</p>
						<p v-else class="portrait-p">나레이션</p>
					</div>
					<p v-if="2 in status">
						어떻게 저렇게 줄어들었지?
					</p>
					<p v-else-if="1 in status">
						여우는 할머니 모습으로 산을 내려갔어요.\n그리고 혼례가 열리는
						잔칫집으로 쏙 들어갔어요!
					</p>
				</div>
			</div>
		</div>
		<nav class="story-btn">
			<!-- <a id="bb-nav-first" href="#" class="bb-custom-icon bb-custom-icon-first"
				>First page</a
			>
			<a
				id="bb-nav-prev"
				href="#"
				class="bb-custom-icon bb-custom-icon-arrow-left"
				>Previous</a
			> -->
			<a
				id="bb-nav-next"
				href="#"
				class="bb-custom-icon bb-custom-icon-arrow-right"
				>Next</a
			>
			<!-- <a id="bb-nav-last" href="#" class="bb-custom-icon bb-custom-icon-last"
				>Last page</a
			> -->
		</nav>
	</div>
</template>

<script src="https://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js"></script>
<script>
import { fetchSubStories } from '@/api/story';
import StoryTextItem from '@/components/story/StoryTextItem.vue';
export default {
	props: {
		myStoryId: Number,
		subStoryId: Number,
	},
	components: {
		StoryTextItem,
	},
	data() {
		return {
			stories: {},
			branch: [
				{
					id: 1,
					question: '여우를 따라갈까? 토끼를 따라갈까?',
					back_image: ' ',
				},
				{
					id: 2,
					question: '마을 안 쪽으로갈까? 여행을 계속할까?',
					back_image: ' ',
				},
				{
					id: 3,
					question: '토끼랑 함께갈까? 여행을 계속할까?',
					back_image: ' ',
				},
				{
					id: 4,
					question: '다음은 어디로 가지?',
					back_image: ' ',
				},
				{
					id: 5,
					question: '큰 나무가 있는곳? 빌딩이 있는곳?',
					back_image: ' ',
				},
				{
					id: 6,
					question: '피리? 기타?',
					back_image: ' ',
				},
			],
			select: [
				{
					id: 1,
					select: '여우를 따라간다',
					substory_id: 3,
					branch_id: 1,
				},
				{
					id: 2,
					select: '토끼를 따라간다',
					substory_id: 5,
					branch_id: 1,
				},
				{
					id: 3,
					select: '마을 안 쪽으로 간다',
					substory_id: 8,
					branch_id: 2,
				},
				{
					id: 4,
					select: '여행을 계속한다',
					substory_id: 10,
					branch_id: 2,
				},
				{
					id: 5,
					select: '토끼랑 함께한다',
					substory_id: 13,
					branch_id: 3,
				},
				{
					id: 6,
					select: '여행을 계속한다',
					substory_id: 10,
					branch_id: 3,
				},
				{
					id: 7,
					select: '마을을 좀 더 구경한다',
					substory_id: 17,
					branch_id: 4,
				},
				{
					id: 8,
					select: '강이 보이는쪽으로 간다',
					substory_id: 19,
					branch_id: 4,
				},
				{
					id: 9,
					select: '큰 나무 쪽으로 간다',
					substory_id: 20,
					branch_id: 5,
				},
				{
					id: 10,
					select: '빌딩 쪽으로 간다',
					substory_id: 24,
					branch_id: 5,
				},
				{
					id: 11,
					select: '피리',
					substory_id: 25,
					branch_id: 6,
				},
				{
					id: 12,
					select: '기타',
					substory_id: 27,
					branch_id: 6,
				},
			],

			status: [],
		};
	},
	methods: {
		async createSubStory() {
			try {
				const { data } = await fetchSubStories(1);
				console.log(data);
				this.stories = data;
			} catch (error) {
				console.log(error);
			}
		},
		hideButton() {
			const btns = document.querySelector('.story-btn');
			btns.style.display = 'none';
		},
		openButton() {
			const btns = document.querySelector('.story-btn');
			btns.style.display = 'inline';
		},
		firstChoice() {
			this.status.push(1);
			setTimeout(function() {
				document.dispatchEvent(new KeyboardEvent('keypress', { keyCode: 39 }));
				const btns = document.querySelector('.story-btn');
				btns.style.display = 'none';
			}, 500);
		},
		secondChoice() {
			this.status.push(2);
			setTimeout(function() {
				document.dispatchEvent(new KeyboardEvent('keypress', { keyCode: 39 }));
				const btns = document.querySelector('.story-btn');
				btns.style.display = 'none';
			}, 500);
		},
		fetchConfig() {
			var Page = (function() {
				var config = {
						$bookBlock: $('#bb-bookblock'),
						$navNext: $('#bb-nav-next'),
						$navPrev: $('#bb-nav-prev'),
						$navFirst: $('#bb-nav-first'),
						$navLast: $('#bb-nav-last'),
					},
					init = function() {
						config.$bookBlock.bookblock({
							speed: 1000,
							shadowSides: 0.8,
							shadowFlip: 0.4,
						});
						initEvents();
					},
					initEvents = function() {
						var $slides = config.$bookBlock.children();
						// add navigation events
						config.$navNext.on('click touchstart', function() {
							config.$bookBlock.bookblock('next');
							return false;
						});

						config.$navPrev.on('click touchstart', function() {
							config.$bookBlock.bookblock('prev');
							return false;
						});

						config.$navFirst.on('click touchstart', function() {
							config.$bookBlock.bookblock('first');
							return false;
						});

						config.$navLast.on('click touchstart', function() {
							config.$bookBlock.bookblock('last');
							return false;
						});

						// add swipe events
						$slides.on({
							swipeleft: function(event) {
								config.$bookBlock.bookblock('next');
								return false;
							},
							swiperight: function(event) {
								config.$bookBlock.bookblock('prev');
								return false;
							},
						});
						// add keyboard events
						$(document).keydown(function(e) {
							var keyCode = e.keyCode || e.which,
								arrow = {
									left: 37,
									up: 38,
									right: 39,
									down: 40,
								};

							switch (keyCode) {
								case arrow.left:
									config.$bookBlock.bookblock('prev');
									break;
								case arrow.right:
									config.$bookBlock.bookblock('next');
									// console.log(arrow.right);
									break;
							}
						});
					};
				return { init: init };
			})();
			Page.init();
		},
	},
	created() {
		this.createSubStory();
	},
	mounted() {
		// const textbtn = document.querySelector('.text-btn');
		// textbtn.style.display = 'none';
		const storyElems = document.querySelectorAll('.bb-item');
		this.currentItem = storyElems[0];
		let ioIndex;
		//eslint-disable-next-line
		const io = new IntersectionObserver((entries, observer) => {
			entries.map(entry => {
				if (entry.isIntersecting) {
					if (entry.target.classList.contains('before-select')) {
						this.hideButton();
						// textbtn.style.display = 'inline';
					} else if (entry.target.classList.contains('after-select')) {
						this.openButton();
						// textbtn.style.display = 'none';
					}
				}
			});
		});
		for (let i = 0; i < storyElems.length; i++) {
			io.observe(storyElems[i]);
		}
		document.addEventListener('keypress', event => {
			if (event.keyCode === 39) {
				$('#bb-bookblock').bookblock('next');
			} else if (event.keyCode === 37) {
				$('#bb-bookblock').bookblock('prev');
			}
		});
		this.fetchConfig();
	},
};
</script>
<style lang="scss">
.bb-custom-side {
	display: flex;
	flex-direction: column;
	justify-content: center;
	align-items: center;
}
.first-cover {
	width: 50%;
}
.portrait-box {
	display: flex;
	flex-direction: column;
	justify-content: center;
	align-items: center;
	.portrait-img {
		width: 30%;
		border-radius: 50%;
		border: 1px solid black;
	}
	.portrait-p {
		text-align: center;
	}
}
.img-side {
	position: relative;
	height: 100%;
	width: 50%;
	img {
		width: 500px;
	}
}
.btn {
	width: 250px;
	height: 120px;
	color: white;
	font-size: 3rem;
	border-radius: 45px;
	border: none;
	&:hover {
		cursor: pointer;
		background: $green;
	}
}
.btn-1 {
	background: $lightGreen !important;
}
.btn-2 {
	background: $orange !important;

	margin-right: 0rem;
}
.bb-black {
	background-color: black !important;
}
.bb-img-character {
	position: absolute;
	top: 10%;
	left: 10%;
	z-index: 10;
}
</style>
