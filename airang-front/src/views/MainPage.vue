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
		<!-- <section>
			<button @click="btnEvent">클릭</button>
		</section> -->
	</section>
</template>

<script>
export default {
	// mounted() {
	// 	const guideElems = document.querySelectorAll('.guide');
	// 	let currentItem;

	// 	for (let i = 0; i < guideElems.length; i++) {
	// 		guideElems[i].dataset.index = i;
	// 	}

	// 	window.addEventListener('scroll', () => {
	// 		let guide;
	// 		let boundingRect;
	// 		for (let i = 0; i < guideElems.length; i++) {
	// 			guide = guideElems[i];
	// 			boundingRect = guide.getBoundingClientRect();
	// 			if (
	// 				boundingRect.top > window.innerHeight * 0.1 &&
	// 				boundingRect.top < window.innerHeight * 0.8
	// 			) {
	// 				console.log(boundingRect.top, window.innerHeight);
	// 				console.log(guide.dataset.index);
	// 				if (currentItem) {
	// 					currentItem.classList.remove('visible');
	// 				}
	// 				currentItem = guideElems[guide.dataset.index];
	// 				console.log(currentItem);
	// 				currentItem.classList.add('visible');
	// 			}
	// 		}
	// 	});
	// },
	mounted() {
		//eslint-disable-next-line
    var controller = new ScrollMagic.Controller();
		//eslint-disable-next-line
		var wipeAnimation = new TimelineMax()
			// animate to second
			.to('.guide-box', 1, { z: -180 })
			.to('.guide-box', 1, { x: '-20%' })
			.to('.guide-box', 1, { z: 0 })
			// animate to third
			.to('.guide-box', 1, { z: -180, delay: 0.6 })
			.to('.guide-box', 1, { x: '-40%' })
			.to('.guide-box', 1, { z: 0 })
			// animate to forth
			.to('.guide-box', 1, { z: -180, delay: 0.6 })
			.to('.guide-box', 1, { x: '-60%' })
			.to('.guide-box', 1, { z: 0 })
			// animate
			.to('.guide-box', 1, { z: -180, delay: 0.6 })
			.to('.guide-box', 1, { x: '-80%' })
			.to('.guide-box', 1, { z: 0 });
		//eslint-disable-next-line
		var scene = new ScrollMagic.Scene({
			triggerElement: '.guide-wrap',
			triggerHook: 'onLeave',
			duration: '400%', //이 값이 클 수록 천천히 덮어씀
		})
			.setPin('.guide-wrap')
			.setTween(wipeAnimation)
			.addIndicators()
			.addTo(controller);
	},
};
</script>

<style lang="scss">
.guide-wrap {
	width: 100%;
	height: 100vh;
	overflow: hidden;
	-webkit-perspective: 1000;
	perspective: 1000;
}
.guide-box {
	width: 500%; // 100*4 slides
	height: 100vh;
}
.guide {
	float: left;
	width: 20%; // 400/25 = 100%
	height: 100vh;
	font-size: 2rem;
	text-align: center;
	color: #fff;
	transition: all 0.5s;
}
.guide-img {
	max-width: 100%;
	height: auto;
}
</style>
