<template>
	<div class="bb-custom-wrapper">
		<div id="bb-bookblock" class="bb-bookblock">
			<div class="bb-item">
				<div class="bb-custom-firstpage">
					<h1>BookBlock <span>A Content Flip Plugin</span></h1>
					<nav class="codrops-nav">
						<a
							class="codrops-icon codrops-icon-prev"
							href="http://tympanus.net/codrops/2012/08/29/multiple-area-charts-with-d3-js/"
							><span>Previous Demo</span></a
						>
						<a
							class="codrops-icon codrops-icon-drop"
							href="http://tympanus.net/codrops/2012/09/03/bookblock-a-content-flip-plugin/"
							><span>Back to the Codrops Article</span></a
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
					<img src="@/assets/images/temp/5.jpg" alt="img" />
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
					<img src="@/assets/images/temp/5.jpg" alt="img" />
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
					<img src="@/assets/images/temp/5.jpg" alt="img" />
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
					<img src="@/assets/images/temp/5.jpg" alt="img" />
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
		this.fetchConfig();
	},
};
</script>
