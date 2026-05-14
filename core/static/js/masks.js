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

document.addEventListener('DOMContentLoaded', function () {
    const cepInputs = document.querySelectorAll('input[name="cep"]');

    cepInputs.forEach((cepInput) => {
        let ultimoCepBuscado = '';

        cepInput.addEventListener('input', async function () {
            const cep = this.value.replace(/\D/g, '');

            if (cep.length !== 8) {
                ultimoCepBuscado = '';
                return;
            }

            if (cep === ultimoCepBuscado) {
                return;
            }

            ultimoCepBuscado = cep;

            try {
                const response = await fetch(`https://viacep.com.br/ws/${cep}/json/`);
                const data = await response.json();

                if (data.erro) {
                    alert('CEP não encontrado.');
                    return;
                }

                const form = cepInput.closest('form');

                if (!form) return;

                const rua = form.querySelector('input[name="rua"]');
                const bairro = form.querySelector('input[name="bairro"]');
                const cidade = form.querySelector('input[name="cidade"]');
                const uf = form.querySelector('input[name="uf"]');

                if (rua) rua.value = data.logradouro || '';
                if (bairro) bairro.value = data.bairro || '';
                if (cidade) cidade.value = data.localidade || '';
                if (uf) uf.value = data.uf || '';

            } catch (error) {
                alert('Erro ao buscar CEP. Verifique sua conexão.');
            }
        });
    });
});