<template>
	<section class="modify-wrap">
		<div class="input-box">
			<span>
				<img class="decoration" src="@/assets/images/sp.png" alt="" />이메일
			</span>
			<input class="input-form" type="text" />
		</div>
		<div class="input-box">
			<span class="">
				<img class="decoration" src="@/assets/images/sp.png" alt="" />이름
			</span>
			<input class="input-form" type="text" />
		</div>
		<div class="input-box">
			<span class="">
				<img class="decoration" src="@/assets/images/sp.png" alt="" />비밀번호
			</span>
			<input class="input-form" type="text" />
		</div>
		<div class="input-box">
			<span class="">
				<img class="decoration" src="@/assets/images/sp.png" alt="" />비밀번호
				확인
			</span>
			<input class="input-form" type="text" />
		</div>
		<footer class="modify-footer"></footer>
	</section>
</template>

<script>
export default {};
</script>

<style lang="scss" scoped>
.modify-wrap {
	padding-left: 7rem;
	padding-right: 7rem;
	margin-top: 4rem;
	.input-box {
		margin-bottom: 2rem;
		display: flex;
		flex-direction: column;
		align-items: center;
		span {
			font-size: 1rem;
			position: relative;
			margin-right: 35%;
		}
		.decoration {
			position: absolute;
			top: -7px;
			left: 0;
			width: 15px;
		}
		.input-form {
			margin-top: 3px;
			width: 50%;
			height: 3rem;
			padding-left: 1rem;
			padding-right: 1rem;
			border-radius: 1rem;
			border: none;
			font-size: 1rem;
		}
	}
	.modify-footer {
		height: 50px;
	}
}
</style>
