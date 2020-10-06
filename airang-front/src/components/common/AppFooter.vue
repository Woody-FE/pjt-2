<template>
	<footer class="footer-wrap">
		<p class="copy">
			<span>copyright</span> &copy; 아이랑 <br />김태인 임창묵 이종우 주재성
			홍연주 황영준
		</p>
		<p class="team"></p>
	</footer>
</template>

<script>
export default {};
</script>

<style lang="scss">
.footer-wrap {
	height: 100px;
	display: grid;
	place-items: center;
	padding: 7px 0;
	font-family: 'KOMACON';
	text-align: center;
	p {
		color: rgb(99, 68, 39);
		font-size: 0.9rem;
	}
	.copy {
		span {
			font-weight: bold;
		}
	}
}
</style>
