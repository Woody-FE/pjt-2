<template>
	<section class="guide-wrap">
		<section class="guide-box">
			<!-- <figure class="guide">
				<img
					class="guide-img"
					src="@/assets/images/00.png"
					alt="첫번째 가이드 이미지"
				/>
				<figcaption class="guide-description">
					않는 눈이 그들의 전인 약동하다. 얼마나 안고, 이 구하지 미인을 모래뿐일
					그들의 뼈 이것이다. 피는 있는 우리 수 말이다. 되려니와, 가진 원질이
					우는 열매를 청춘은 끝에 부패뿐이다. 얼마나 없으면 노래하며 수 그들을
					관현악이며, 살 보이는 우리 약동하다.
				</figcaption>
			</figure> -->
			<figure class="guide">
				<img
					class="guide-img"
					src="@/assets/images/01.png"
					alt="두번째 가이드 이미지"
				/>
				<figcaption class="guide-description">
					않는 눈이 그들의 전인 약동하다. 얼마나 안고, 이 구하지 미인을 모래뿐일
					그들의 뼈 이것이다. 피는 있는 우리 수 말이다. 되려니와, 가진 원질이
					우는 열매를 청춘은 끝에 부패뿐이다. 얼마나 없으면 노래하며 수 그들을
					관현악이며, 살 보이는 우리 약동하다.
				</figcaption>
			</figure>
			<figure class="guide">
				<img
					class="guide-img"
					src="@/assets/images/02.png"
					alt="첫번째 가이드 이미지"
				/>
				<figcaption class="guide-description">
					않는 눈이 그들의 전인 약동하다. 얼마나 안고, 이 구하지 미인을 모래뿐일
					그들의 뼈 이것이다. 피는 있는 우리 수 말이다. 되려니와, 가진 원질이
					우는 열매를 청춘은 끝에 부패뿐이다. 얼마나 없으면 노래하며 수 그들을
					관현악이며, 살 보이는 우리 약동하다.
				</figcaption>
			</figure>
			<figure class="guide">
				<img
					class="guide-img"
					src="@/assets/images/03.png"
					alt="첫번째 가이드 이미지"
				/>
				<figcaption class="guide-description">
					않는 눈이 그들의 전인 약동하다. 얼마나 안고, 이 구하지 미인을 모래뿐일
					그들의 뼈 이것이다. 피는 있는 우리 수 말이다. 되려니와, 가진 원질이
					우는 열매를 청춘은 끝에 부패뿐이다. 얼마나 없으면 노래하며 수 그들을
					관현악이며, 살 보이는 우리 약동하다.
				</figcaption>
			</figure>
			<figure class="guide">
				<img
					class="guide-img"
					src="@/assets/images/04.png"
					alt="첫번째 가이드 이미지"
				/>
				<figcaption class="guide-description">
					않는 눈이 그들의 전인 약동하다. 얼마나 안고, 이 구하지 미인을 모래뿐일
					그들의 뼈 이것이다. 피는 있는 우리 수 말이다. 되려니와, 가진 원질이
					우는 열매를 청춘은 끝에 부패뿐이다. 얼마나 없으면 노래하며 수 그들을
					관현악이며, 살 보이는 우리 약동하다.
				</figcaption>
			</figure>
			<figure class="guide">
				<img
					class="guide-img"
					s
					src="@/assets/images/05.png"
					alt="첫번째 가이드 이미지"
				/>
				<figcaption class="guide-description">
					않는 눈이 그들의 전인 약동하다. 얼마나 안고, 이 구하지 미인을 모래뿐일
					그들의 뼈 이것이다. 피는 있는 우리 수 말이다. 되려니와, 가진 원질이
					우는 열매를 청춘은 끝에 부패뿐이다. 얼마나 없으면 노래하며 수 그들을
					관현악이며, 살 보이는 우리 약동하다.
				</figcaption>
			</figure>
		</section>
		<section>
			<button class="guide-btn">V</button>
		</section>
	</section>
</template>

<script>
export default {
	data() {
		return {
			windowTop: 0,
		};
	},
	mounted() {
		const guideElems = document.querySelectorAll('.guide');
		let currentItem;
		for (let i = 0; i < guideElems.length; i++) {
			guideElems[i].dataset.index = i;
		}
		const btn = document.querySelector('.guide-btn');
		btn.addEventListener('click', () => {
			let guide;
			let boundingRect;
			if (
				document.querySelector('body').scrollHeight <=
				this.windowTop + window.innerHeight + 100
			) {
				return;
			}
			for (let i = 0; i < guideElems.length; i++) {
				guide = guideElems[i];
				boundingRect = guide.getBoundingClientRect();
				if (boundingRect.bottom === window.innerHeight) {
					if (
						currentItem &&
						currentItem !== guideElems[guideElems.length - 1]
					) {
						currentItem.classList.remove('visible');
					}

					currentItem = guideElems[i + 1];
					currentItem.classList.add('visible');
				}
			}
			window.scrollBy({
				top: window.innerHeight,
				behavior: 'smooth',
			});
		});
		window.addEventListener('wheel', event => {
			this.windowTop = window.scrollY;
			var delta;
			if (event.wheelDelta) {
				delta = event.wheelDelta;
			} else {
				delta = -1 * event.deltaY;
			}
			let guide;
			let boundingRect;

			if (delta < 0) {
				for (let i = 0; i < guideElems.length; i++) {
					guide = guideElems[i];
					boundingRect = guide.getBoundingClientRect();
					if (
						boundingRect.top > window.innerHeight * 0.1 &&
						boundingRect.top < window.innerHeight * 0.15
					) {
						if (currentItem) {
							currentItem.classList.remove('visible');
						}
						currentItem = guide;
						currentItem.classList.add('visible');
					}
				}
			} else if (delta > 0) {
				for (let i = 0; i < guideElems.length; i++) {
					guide = guideElems[i];
					boundingRect = guide.getBoundingClientRect();
					if (boundingRect.bottom === window.innerHeight) {
						if (currentItem) {
							currentItem.classList.remove('visible');
						}
						currentItem = guide;
						currentItem.classList.add('visible');
					}
				}
			}
		});
		// function findScrollDirectionOtherBrowsers(event) {
		// 	this.windowTop = window.scrollY;

		// 	var delta;
		// 	if (event.wheelDelta) {
		// 		delta = event.wheelDelta;
		// 	} else {
		// 		delta = -1 * event.deltaY;
		// 	}
		// 	let guide;
		// 	let boundingRect;

		// 	if (delta < 0) {
		// 		for (let i = 0; i < guideElems.length; i++) {
		// 			guide = guideElems[i];
		// 			boundingRect = guide.getBoundingClientRect();
		// 			if (
		// 				boundingRect.top > window.innerHeight * 0.1 &&
		// 				boundingRect.top < window.innerHeight * 0.15
		// 			) {
		// 				if (currentItem) {
		// 					currentItem.classList.remove('visible');
		// 				}
		// 				currentItem = guide;
		// 				currentItem.classList.add('visible');
		// 			}
		// 		}
		// 	} else if (delta > 0) {
		// 		for (let i = 0; i < guideElems.length; i++) {
		// 			guide = guideElems[i];
		// 			boundingRect = guide.getBoundingClientRect();
		// 			if (boundingRect.bottom === window.innerHeight) {
		// 				if (currentItem) {
		// 					currentItem.classList.remove('visible');
		// 				}
		// 				currentItem = guide;
		// 				currentItem.classList.add('visible');
		// 			}
		// 		}
		// 	}
		// }
	},
};
</script>

<style lang="scss">
.guide-wrap {
	width: 100%;
	height: 100%;
}
.guide-box {
	width: 100%;
	height: 500vh;
	scroll-snap-type: y mandatory;
}
.guide {
	position: sticky;
	top: 0;
	left: 0;
	width: 100%;
	height: 100vh;
	font-size: 2rem;
	text-align: center;
	color: #fff;
	opacity: 0;
	transition: all 0.5s;
	scroll-snap-align: start;
	will-change: opacity;
}
.guide-img {
	max-width: 100%;
	height: auto;
}
.visible {
	opacity: 1;
}
.guide-btn {
	position: fixed;
	bottom: 0;
	right: 0;
}
</style>
