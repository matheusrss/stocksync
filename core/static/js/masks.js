document.addEventListener('DOMContentLoaded', function () {
    if (typeof IMask === 'undefined') {
        console.warn('IMask não foi carregado.');
        return;
    }

    document.querySelectorAll('.mask-cpf').forEach((campo) => {
        IMask(campo, {
            mask: '000.000.000-00'
        });
    });

    document.querySelectorAll('.mask-cnpj').forEach((campo) => {
        IMask(campo, {
            mask: '00.000.000/0000-00'
        });
    });

    document.querySelectorAll('.mask-cpf-cnpj').forEach((campo) => {
        IMask(campo, {
            mask: [
                {
                    mask: '000.000.000-00',
                    maxLength: 11
                },
                {
                    mask: '00.000.000/0000-00'
                }
            ]
        });
    });

    document.querySelectorAll('.mask-telefone').forEach((campo) => {
        IMask(campo, {
            mask: '(00) 0000-0000'
        });
    });

    document.querySelectorAll('.mask-celular').forEach((campo) => {
        IMask(campo, {
            mask: '(00) 00000-0000'
        });
    });

    document.querySelectorAll('.mask-cep').forEach((campo) => {
        IMask(campo, {
            mask: '00000-000'
        });
    });

    document.querySelectorAll('.mask-uf').forEach((campo) => {
        campo.addEventListener('input', function () {
            this.value = this.value.toUpperCase().replace(/[^A-Z]/g, '').slice(0, 2);
        });
    });
});