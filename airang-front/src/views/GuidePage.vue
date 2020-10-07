<template>
	<section class="guide-wrap">
		<section class="guide-box">
			<figure class="guide visible">
				<figcaption class="guide-description">
					<p>회원가입의 아이 이름이 주인공의 이름이 되어요.</p>
				</figcaption>
				<img
					class="guide-img guide-first-img"
					src="@/assets/images/guide/guide_img_1.png"
					alt="첫 번째 가이드 이미지"
				/>
			</figure>
			<figure class="guide">
				<figcaption class="guide-description">
					<p>만들고 싶은 동화를 골라주세요 :)</p>
				</figcaption>
				<img
					class="guide-img"
					src="@/assets/images/guide/guide_img_2.png"
					alt="두 번째 가이드 이미지"
				/>
			</figure>
			<figure class="guide">
				<figcaption class="guide-description">
					<p>나만의 제목을 정해주세요</p>
					<p>내 얼굴을 동화에 맞게 바꿔줍니다!</p>
				</figcaption>
				<img
					class="guide-img"
					src="@/assets/images/guide/guide_img_3.png"
					alt="세 번째 가이드 이미지"
				/>
			</figure>
			<figure class="guide">
				<figcaption class="guide-description">
					<p>분기점에 따라 이야기가 바뀌어요!</p>
				</figcaption>
				<img
					class="guide-img"
					src="@/assets/images/guide/guide_img_4.png"
					alt="네 번째 가이드 이미지"
				/>
			</figure>
			<figure class="guide">
				<figcaption class="guide-description">
					<p>선택지들 마다 다른 엔딩이 있어요!</p>
					<p>궁금하지 않나요?</p>
				</figcaption>
				<img
					class="guide-img guide-last-img"
					src="@/assets/images/guide/guide_img_5.png"
					alt="다섯 번째 가이드 이미지"
				/>
			</figure>
			<figure class="guide-end-box">
				<button class="guide-end-btn" @click="clickEndBtn">
					동화책 주인공이 되어 보실래요?
				</button>
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
import { mapGetters } from 'vuex';
export default {
	data() {
		return {
			windowTop: 0,
			currentItem: null,
		};
	},
	methods: {
		...mapGetters(['isLogined']),
		topScroll() {
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
			const downbtn = document.querySelector('.guide-btn__down');
			downbtn.style.display = 'inline';
		},
		clickEndBtn() {
			if (this.isLogined) {
				this.$router.push('/login?guide=true');
			} else {
				this.$router.push('/bookshelf');
			}
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
		let ioIndex;
		//eslint-disable-next-line
        const io = new IntersectionObserver((entries, observer) => {
			ioIndex = entries[0].target.dataset.index * 1;
		});
		for (let i = 0; i < guideElems.length; i++) {
			io.observe(guideElems[i]);
			guideElems[i].dataset.index = i;
		}
		const downbtn = document.querySelector('.guide-btn__down');
		downbtn.addEventListener('click', () => {
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
				downbtn.style.display = 'none';
				return;
			}
			downbtn.style.display = 'inline';
			for (let i = ioIndex - 1; i < ioIndex + 2; i++) {
				if (i === guideElems.length - 1) {
					break;
				}
				guide = guideElems[i];
				if (!guide) continue;
				boundingRect = guide.getBoundingClientRect();
				if (parseInt(boundingRect.bottom) === window.innerHeight) {
					this.currentItem.classList.remove('visible');
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
				for (let i = ioIndex - 1; i < ioIndex + 2; i++) {
					guide = guideElems[i];
					if (!guide) continue;
					boundingRect = guide.getBoundingClientRect();
					if (
						boundingRect.top > window.innerHeight * 0.1 &&
						boundingRect.top < window.innerHeight * 0.2
					) {
						this.currentItem.classList.remove('visible');
						this.currentItem = guide;
						this.currentItem.classList.add('visible');
					}
				}
			} else if (delta > 0) {
				for (let i = 0; i < guideElems.length; i++) {
					guide = guideElems[i];
					boundingRect = guide.getBoundingClientRect();
					if (parseInt(boundingRect.bottom) === window.innerHeight) {
						this.currentItem.classList.remove('visible');
						this.currentItem = guide;
						this.currentItem.classList.add('visible');
					}
				}
				downbtn.style.display = 'inline';
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
	flex-direction: column;
	justify-content: center;
	align-items: center;
	position: sticky;
	top: 0;
	left: 0;
	width: 100%;
	height: 100vh;
	font-size: 2rem;
	text-align: center;
	color: black;
	opacity: 0;
	transition: all 1s;
	will-change: opacity;
}
.guide-description {
	margin-bottom: 5%;
	font-family: 'KOMACON';
}
.guide-img {
	max-width: 50%;
	height: auto;
}
.guide-first-img {
	width: 50%;
}
.guide-last-img {
	width: 40%;
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
	background: linear-gradient(0deg, #ff922b, #faad08);
	color: white;
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
	background: linear-gradient(0deg, #ff922b, #faad08);
	color: white;
	outline: none;
}
.guide-end-box {
	display: relative;
	width: 100%;
	display: flex;
	flex-direction: column;
	align-items: center;
}
.guide-end-btn {
	position: flex;
	justify-content: flex-start;
	align-items: center;
	width: 50%;
	height: 3.5rem;
	font-size: 3rem;
	border-top-left-radius: 1.5rem;
	border-bottom-left-radius: 1.5rem;
	border-top-right-radius: 1.5rem;
	border-bottom-right-radius: 1.5rem;
	outline: none;
	border: none;
	cursor: pointer;
	font-size: 1rem;
	font-weight: bold;
	color: white;
	background-color: #2f9e44;
	margin-bottom: 3rem;
}
</style>
