<template>
	<section class="guide-wrap">
		<section class="guide-box">
			<figure class="guide visible">
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
			<button class="guide-btn__down">
				<i class="icon ion-md-arrow-down"></i>
			</button>
			<button class="guide-btn__top" @click="topScroll">TOP</button>
		</section>
	</section>
</template>

<script>
export default {
	data() {
		return {
			windowTop: 0,
			currentItem: null,
		};
	},
	methods: {
		topScroll() {
			// const guideElems = document.querySelectorAll('.guide');
			// console.log(guideElems[0].getBoundingClientRect().top);
			// window.scrollTo({
			// 	top: guideElems[0].getBoundingClientRect().top,
			// 	behavior: 'smooth',
			// });
			// guideElems[0].classList.add('visible');
			this.currentItem.classList.remove('visible');
			setTimeout(() => {
				scrollTo({
					top: 0,
					behavior: 'smooth',
				});
			}, 100);
			const guideElems = document.querySelectorAll('.guide');
			this.currentItem = guideElems[0];
			this.currentItem.classList.add('visible');
		},
	},
	mounted() {
		window.addEventListener('load', () => {
			setTimeout(() => {
				scrollTo(0, 0);
			}, 100);
		});
		const guideElems = document.querySelectorAll('.guide');
		this.currentItem = guideElems[0];
		for (let i = 0; i < guideElems.length; i++) {
			guideElems[i].dataset.index = i;
		}
		const btn = document.querySelector('.guide-btn__down');
		btn.addEventListener('click', () => {
			let guide;
			let boundingRect;
			window.scrollBy({
				top: window.innerHeight,
				behavior: 'smooth',
			});
			this.windowTop = window.scrollY;
			if (
				document.querySelector('body').scrollHeight <=
				this.windowTop + window.innerHeight
			) {
				return;
			}
			for (let i = 0; i < guideElems.length; i++) {
				guide = guideElems[i];
				boundingRect = guide.getBoundingClientRect();
				if (boundingRect.bottom === window.innerHeight) {
					if (
						this.currentItem &&
						this.currentItem !== guideElems[guideElems.length - 1]
					) {
						this.currentItem.classList.remove('visible');
					}

					this.currentItem = guideElems[i + 1];
					this.currentItem.classList.add('visible');
				}
			}
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
						boundingRect.top < window.innerHeight * 0.2
					) {
						if (this.currentItem) {
							this.currentItem.classList.remove('visible');
						}
						this.currentItem = guide;
						this.currentItem.classList.add('visible');
					}
				}
			} else if (delta > 0) {
				for (let i = 0; i < guideElems.length; i++) {
					guide = guideElems[i];
					boundingRect = guide.getBoundingClientRect();
					if (boundingRect.bottom === window.innerHeight) {
						if (this.currentItem) {
							this.currentItem.classList.remove('visible');
						}
						this.currentItem = guide;
						this.currentItem.classList.add('visible');
					}
				}
			}
		});
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
}
.guide {
	display: flex;
	justify-content: space-evenly;
	align-items: center;
	position: sticky;
	top: 0;
	left: 0;
	width: 100%;
	height: 100vh;
	font-size: 2rem;
	text-align: center;
	color: #fff;
	opacity: 0;
	transition: all 1s;
	will-change: opacity;
}
.guide-img {
	max-width: 50%;
	height: auto;
}
.visible {
	opacity: 1;
}
.guide-btn__down {
	position: fixed;
	top: 50%;
	right: 2rem;
	width: 3rem;
	height: 3rem;
	font-size: 2rem;
	border: none;
	cursor: pointer;
	border-radius: 50%;
	background: white;
	outline: none;
	margin-left: -1rem;
}
.guide-btn__top {
	position: fixed;
	bottom: 2rem;
	right: 2rem;
	width: 3rem;
	height: 3rem;
	font-size: 1rem;
	border: none;
	cursor: pointer;
	border-radius: 50%;
	background: white;
	outline: none;
}
</style>
