<template>
	<section class="mystory-wrap">
		<div class="mystory-bookcover">
			<section class="mystory-page">
				<div class="mystory-face mystory-cover">
					<!-- 팀 소개책 커버 이미지 -->
					<img
						class="mystory-cover__img"
						src="@/assets/images/bookShelf/friendsBook.jpg"
						alt=""
					/>
				</div>
				<div class="mystory-face">
					<div class="member-box">
						<img
							class="member-img__bg"
							src="@/assets/images/bg/bg_tae.png"
							alt=""
						/>
						<img
							class="member-img"
							src="@/assets/images/user/taein.png"
							alt=""
						/>
						<div class="member-content">
							<p>김태인(9)</p>
							<p>Frontend & Reader<br />& UCC editor</p>
							<p>메리랑 아이랑 제일 좋아</p>
						</div>
					</div>
					<div class="member-box">
						<img
							class="member-img__bg"
							src="@/assets/images/bg/bg_jong.png"
							alt=""
						/>
						<img
							class="member-img"
							src="@/assets/images/user/jongwoo.png"
							alt=""
						/>
						<div class="member-content">
							<p>이종우(5)</p>
							<p>Backend & Frontend<br />& Illustrator</p>
							<p>동화책 한 권 할래?</p>
						</div>
					</div>
					<div class="member-box">
						<img
							class="member-img__bg"
							src="@/assets/images/bg/bg_chang.png"
							alt=""
						/>
						<img
							class="member-img"
							src="@/assets/images/user/changmuk.png"
							alt=""
						/>
						<div class="member-content">
							<p>임창묵(6)</p>
							<p>AI & Presenter<br />& UCC director</p>
							<p style="font-size:1.1rem !important">
								역시 AIrang이야 성능확실하구만
							</p>
						</div>
					</div>
				</div>
			</section>
			<section class="mystory-page">
				<div class="mystory-face">
					<div class="member-box">
						<img
							class="member-img__bg"
							src="@/assets/images/bg/bg_jae.png"
							alt=""
						/>
						<img
							class="member-img"
							src="@/assets/images/user/jaesung.png"
							alt=""
						/>
						<div class="member-content">
							<p>주재성(7)</p>
							<p>AI & Presenter<br />& Support</p>
							<p>너 동화 문제있어?</p>
						</div>
					</div>
					<div class="member-box">
						<img
							class="member-img__bg"
							src="@/assets/images/bg/bg_yeon.png"
							alt=""
						/>
						<img
							class="member-img"
							src="@/assets/images/user/yeonju.png"
							alt=""
						/>
						<div class="member-content">
							<p>홍연주(3)</p>
							<p>Frontend & Illustrator<br />& UCC director</p>
							<p>아이랑 아랑이랑</p>
						</div>
					</div>
					<div class="member-box">
						<img
							class="member-img__bg"
							src="@/assets/images/bg/bg_young.png"
							alt=""
						/>
						<img
							class="member-img"
							src="@/assets/images/user/youngjun.png"
							alt=""
						/>
						<div class="member-content">
							<p>황영준(6)</p>
							<p>Frontend & Writer<br />& Actor</p>
							<p>아이들 어서오고</p>
						</div>
					</div>
				</div>
			</section>
		</div>
	</section>
</template>

<script>
export default {
	mounted() {
		const cover = document.querySelector('.mystory-cover__img');
		if (cover) {
			cover.addEventListener('load', () => {
				const page = document.querySelectorAll('.mystory-page');
				setTimeout(function() {
					page[0].classList.add('flipped');
				}, 750);
			});
		}
	},
};
</script>

<style lang="scss" scoped>
.mystory-wrap {
	position: relative;
	width: 100%;
	min-height: 100vh;
	.mystory-bookcover {
		position: absolute;
		left: 0;
		right: 0;
		top: 0;
		bottom: 0;
		width: 90vw;
		height: 95vh;
		transform-style: preserve-3d;
		margin: auto;
		.mystory-page {
			position: absolute;
			left: 50%;
			top: 0;
			box-shadow: 0 2px 6px 0 rgba(68, 67, 68, 0.4);
			width: 50%;
			height: 100%;
			transform-style: preserve-3d;
			transition: 1s;
			border: 1px solid lightgray;
			.mystory-face {
				position: absolute;
				left: 0;
				box-shadow: 0 2px 6px 0 rgba(68, 67, 68, 0.4);
				top: 0;
				width: 100%;
				height: 100%;
				background: white;
				color: black;
				backface-visibility: hidden;
				.member-box {
					height: 30%;
					display: flex;
					align-items: center;
					position: relative;
					.member-img {
						height: 80%;
						margin-right: 10%;
						margin-left: 10%;
						z-index: 5;
					}
					.member-img__bg {
						position: absolute;
						top: 0;
						left: 0;
						width: 80%;
						height: 70%;
						padding: 10%;
						z-index: 4;
					}
					.member-content {
						height: 100%;
						line-height: 1.5;
						display: flex;
						flex-direction: column;
						justify-content: flex-end;
						z-index: 5;
						margin-bottom: 30px;
						p {
							font-size: 1.3rem;
							font-family: 'KOMACON';
							color: rgb(105, 105, 105);
							@media screen and (max-width: 1024px) {
								font-size: 1rem;
								margin-bottom: 10px;
							}
						}
					}
				}
			}
			&:nth-child(1) {
				z-index: 3;
				transform-origin: left;
			}
			&:nth-child(2) {
				z-index: 2;
				transform-origin: left;
			}
		}
	}
}
.mystory-face:nth-child(2) {
	transform: rotateY(-180deg);
}
.flipped {
	transform: rotateY(-180deg);
}
.mystory-cover {
	width: 100%;
	display: flex;
	justify-content: center;
	align-items: center;
	.mystory-cover__img {
		width: 100%;
		height: 100%;
		object-fit: fill;
	}
}
</style>
