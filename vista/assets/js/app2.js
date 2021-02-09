$(document).ready(function(){

	$('#tipoAsistente').on('change', function(){

		var selectValor = '#'+$(this).val();

		$('#pai').children('div').hide();
		$('#pai').children(selectValor).show();

	});

	$('#llenoSanto').on('change', function(){

		var selectValor = '#'+$(this).val();

		$('#pai2').children('div').hide();
		$('#pai2').children(selectValor).show();

	});

	$('#servidorLocal').on('change', function(){

		var selectValor = '#'+$(this).val();

		$('#pai3').children('div').hide();
		$('#pai3').children(selectValor).show();

	});

});