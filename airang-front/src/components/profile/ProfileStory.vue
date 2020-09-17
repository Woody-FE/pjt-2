<template>
	<section class="profileStory-wrap">
		<header class="profileStory-header">
			<span class="profileStory-header__span"></span>
			<p class="profileStory-header__name">나의 이야기</p>
		</header>
		<section class="profileStory-body">
			<router-link to="/story">
				<div class="profileStory-body__box">
					<article class="profileStory-body__book book1"></article>
					<p class="profileStory-body__name">세가지 선물</p>
				</div>
			</router-link>
			<router-link to="/story">
				<div class="profileStory-body__box">
					<article class="profileStory-body__book book1"></article>
					<p class="profileStory-body__name">세가지 선물</p>
				</div>
			</router-link>
		</section>
		<footer class="profileStory-footer"></footer>
	</section>
</template>

<script>
export default {};
</script>

<style lang="scss">
.profileStory-wrap {
	display: flex;
	flex-direction: column;
	.profileStory-header {
		margin-bottom: 1.5rem;
		display: flex;
		align-content: content;
		.profileStory-header__span {
			display: inline-block;
			width: 3px;
			height: 2rem;
			background: yellow;
			margin-right: 5px;
		}
		.profileStory-header__name {
			font-size: 2rem;
		}
	}
	.profileStory-body {
		z-index: 10;
		width: 720px;
		display: flex;
		flex-direction: row;
		align-items: center;
		.profileStory-body__box {
			display: flex;
			flex-direction: column;
			justify-content: center;
			align-items: center;
			margin-right: 22px;
		}
		.profileStory-body__name {
			margin-bottom: 1rem;
			font-size: 1.5rem;
			color: $deepGray;
			font-weight: 1rem;
		}
		.profileStory-body__book {
			width: 180px;
			height: 255px;
			margin-bottom: 0.5rem;
			background-color: rgb(62, 71, 152);
			transition: all 0.3s ease-in-out;
			transform-origin: left center 0px;
			transform-style: preserve-3d;
			border-top-right-radius: 5px;
			border-bottom-right-radius: 5px;
			-webkit-backface-visibility: hidden;
			overflow: hidden;
		}
		.profileStory-body__book::after {
			content: ' ';
			display: block;
			opacity: 0;
			width: 180px;
			height: 255px;
			position: relative;
			left: 8px;
			transition: all 0.3s ease;
		}
		.profileStory-body__book::before {
			content: ' ';
			z-index: 999;
			display: block;
			width: 20px;
			height: 100px;
			opacity: 0;
			position: absolute;
			top: -12px;
			right: 8px;
			transition: all 0.25s;
			background: url('data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAD8AAABhCAYAAABh23lYAAAACXBIWXMAAAsTAAALEwEAmpwYAAAAAXNSR0IArs4c6QAAAARnQU1BAACxjwv8YQUAAAHCSURBVHgB7dxPTsJAHMXxN7Xu3UhigobxJHACvQFwAr2BcgO8AZxE7uGiDZiQyEIW7oSOUyKbKgLS8u+9b9JNF818fum0XdWUhy9VEDZBGIdBGD6DsFM3bQYgTnjWhGdNeNaEZ0141oRnTXjWhGdNeNaEZ0141oRnTXjWhGdNeNaEZ0141oRnTXjWhGdNeNaEZ0141oRnTXjWhGdNeNaEZ0141oRnTXjWhGdNeNaEZ0141oRnTXjWhGdNeNZ2hR/7o+UcmnCIsaNCbLcU/RR8oB1bO/4+17l8ixoGeIBBBVvMXI0ih+L7Df2j8iiqnvgh+AVVUXDOTZvF4tNb2qC7DJ1tNgSDO78tblFQxeE92l+0NSjZDjaoMowqyYl7hDF15JzL+x+YHtxLgFq/ZO2m8LT4wsb90nUjmMD61XaRc7ng5+jBua29ntsecq6oIWyELxqdLe8h/GvPp+h0T28D/FezZ8Ip7pHgZt3X5NoPvH1BZ5sNIUTDL7C+6hBWxxt0gk+00tsOe96qH0zL8GO4pBtMg/YhoLMtG8Ii/EpfY4fSoiFk8UeFzpYdwhz/jiNGZ0uHEBjUEzftohJFZyAsdX8BM0/amLC3spYAAAAASUVORK5CYII=');
			background-size: 16px;
			background-repeat: no-repeat;
		}

		/* ----- hover ----- */

		.profileStory-body__book:hover {
			cursor: pointer;
			transform: rotateY(-28deg) rotateZ(-2deg) scale(1.02);
			-webkit-backface-visibility: hidden;
			box-shadow: 1px 3px 2px #353d85, 20px 8px 0 #525dc4;
			/* transform: scale(1.02); */
		}

		.profileStory-body__book:hover::after {
			content: ' ';
			display: block;
			opacity: 1;
			width: 172px;
			height: 255px;
			position: relative;
			left: 8px;
			background: linear-gradient(
				-180deg,
				rgba(255, 255, 255, 0.1) 0%,
				rgba(255, 255, 255, 0) 60%
			);
		}
		.profileStory-body__book:hover::before {
			transform: translateY(9px);
			opacity: 1;
		}
		.book1 {
			background: url('https://image.yes24.com/Goods/30586134/L');
			background-size: 180px 255px;
		}
	}
	.profileStory-footer {
		margin-bottom: 3rem;
	}
}
</style>
