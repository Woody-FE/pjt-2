<template>
	<div class="bb-custom-wrapper">
		<div id="bb-bookblock" ref="book" class="bb-bookblock">
			<div class="bb-item">
				<div class="bb-custom-firstpage">
					<img
						class="first-cover"
						src="@/assets/images/아랑이3.jpg"
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
			<div class="bb-item">
				<div class="bb-custom-side img-side">
					<img src="@/assets/images/temp/44.png" alt="img" />
				</div>
				<div class="bb-custom-side">
					<div class="portrait-box">
						<img
							class="portrait-img"
							src="@/assets/images/temp/po.png"
							alt=""
						/>
						<p class="portrait-p">나레이션</p>
					</div>
					<p>
						넓은 세상을 보고싶은 영준이는<br />
						어른이 된날 아버지에게 여행을 떠나겠다고 말했어요
					</p>
				</div>
			</div>
			<div class="bb-item">
				<div class="bb-custom-side img-side">
					<img src="@/assets/images/temp/44.png" alt="img" />
				</div>
				<div class="bb-custom-side">
					<div class="portrait-box">
						<img
							class="portrait-img"
							src="@/assets/images/temp/zoo.png"
							alt=""
						/>
						<p class="portrait-p">아버지</p>
					</div>
					<p>그래, 잘 갔다 와라<br />잘 갔다 와라는 의미로 3가지 선물을 주마</p>
				</div>
			</div>
			<div class="bb-item">
				<div class="bb-custom-side img-side">
					<img src="@/assets/images/temp/44.png" alt="img" />
				</div>
				<div class="bb-custom-side">
					<div class="portrait-box">
						<img
							class="portrait-img"
							src="@/assets/images/temp/po.png"
							alt=""
						/>
						<p class="portrait-p">나레이션</p>
					</div>
					<p>
						아버지에게 3가지 선물을 받은 영준(이)는<br />여행을 떠나기
						시작했어요.
					</p>
				</div>
			</div>
			<div class="bb-item">
				<div class="bb-custom-side img-side">
					<img src="@/assets/images/crossroad.jpg" alt="img" />
				</div>
				<div class="bb-custom-side">
					<div class="portrait-box">
						<img
							class="portrait-img"
							src="@/assets/images/temp/po.png"
							alt=""
						/>
						<p class="portrait-p">나레이션</p>
					</div>
					<p>
						얼마 정도 갔을까<br />길의 한쪽에는 여우가 <br />한쪽에는 토끼가
						있는걸 발견했어요.
					</p>
				</div>
			</div>
			<div class="bb-item">
				<div class="bb-custom-side img-side">
					<button class="btn btn-1" @click="firstChoice">
						여우
					</button>
				</div>
				<div class="bb-custom-side">
					<button class="btn btn-2" @click="secondChoice">토끼</button>
				</div>
			</div>
			<div class="bb-item">
				<div class="bb-custom-side img-side">
					<img
						v-if="status === 1"
						src="@/assets/images/changes.jpg"
						alt="img"
					/>
					<img v-else src="@/assets/images/small.jpg" alt="img" />
				</div>
				<div class="bb-custom-side">
					<div class="portrait-box">
						<img
							class="portrait-img"
							src="@/assets/images/temp/po.png"
							alt=""
						/>
						<p class="portrait-p">나레이션</p>
					</div>
					<p v-if="status === 2">
						토끼는 나무둥지 앞에 멈춰섰어요<br />
						그런데! 갑자기 토끼의 크기가 개미같이 줄어들었어요
					</p>
					<p v-else>
						여우는 할머니 모습으로 산을 내려갔어요.<br />그리고 혼례가 열리는
						잔칫집으로 쏙 들어갔어요!
					</p>
				</div>
			</div>
			<div class="bb-item">
				<div class="bb-custom-side img-side">
					<img
						v-if="status === 1"
						src="@/assets/images/changes.jpg"
						alt="img"
					/>
					<img v-else src="@/assets/images/small.jpg" alt="img" />
				</div>
				<div class="bb-custom-side">
					<div class="portrait-box">
						<img
							v-if="status === 2"
							class="portrait-img"
							src="@/assets/images/temp/12345.png"
							alt=""
						/>
						<img
							v-else
							class="portrait-img"
							src="@/assets/images/temp/po.png"
							alt=""
						/>
						<p v-if="status === 2" class="portrait-p">영준</p>
						<p v-else class="portrait-p">나레이션</p>
					</div>
					<p v-if="status === 2">
						어떻게 저렇게 줄어들었지?
					</p>
					<p v-else>
						여우는 할머니 모습으로 산을 내려갔어요.\n그리고 혼례가 열리는
						잔칫집으로 쏙 들어갔어요!
					</p>
				</div>
			</div>
		</div>
		<nav>
			<a id="bb-nav-first" href="#" class="bb-custom-icon bb-custom-icon-first"
				>First page</a
			>
			<a
				id="bb-nav-prev"
				href="#"
				class="bb-custom-icon bb-custom-icon-arrow-left"
				>Previous</a
			>
			<a
				id="bb-nav-next"
				href="#"
				class="bb-custom-icon bb-custom-icon-arrow-right"
				>Next</a
			>
			<a id="bb-nav-last" href="#" class="bb-custom-icon bb-custom-icon-last"
				>Last page</a
			>
		</nav>
	</div>
</template>

<script src="https://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js"></script>
<script>
export default {
	data() {
		return {
			status: 0,
			cnt: 2,
			bookData: {
				leftData: [],
				rightData: [
					{
						content:
							'넓은 세상을 보고싶은 {child_name}(이)는\n어른이 된 날 아버지에게 여행을 떠나겠다고 말했어요',
						id: 1,
					},
					{
						content: '나는 외안될까요?',
						id: 2,
					},
				],
			},
		};
	},
	methods: {
		firstChoice() {
			this.status = 1;
			setTimeout(function() {
				console.log('선택1!');
				document.dispatchEvent(new KeyboardEvent('keypress', { keyCode: 39 }));
			}, 500);
		},
		secondChoice() {
			this.status = 2;
			setTimeout(function() {
				console.log('선택2!');
				document.dispatchEvent(new KeyboardEvent('keypress', { keyCode: 39 }));
			}, 500);
		},
		fetchNextPage() {
			console.log(this.bookData.rightData.length);
			this.bookData.rightData.push({
				content: '다음페이지를 불러왔어요 잘 되나요???',
				id: ++this.cnt,
			});
			this.fetchConfig();
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
	mounted() {
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
</style>
