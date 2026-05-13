document.addEventListener('DOMContentLoaded', function () {
    console.log('StockSync carregado com sucesso!');

    configurarBuscaLocal();
    configurarSidebarMobile();
    configurarSelecaoCadastros();
    configurarSelecaoProdutos();
    configurarSelecaoContas();
});

function configurarBuscaLocal() {
    const searchInput = document.querySelector('.search-input-custom');
    const tableRows = document.querySelectorAll('.table-cadastro tbody tr');

    if (!searchInput || tableRows.length === 0) return;

    searchInput.addEventListener('input', function () {
        const termo = this.value.toLowerCase();
        tableRows.forEach(function (row) {
            const textoLinha = row.innerText.toLowerCase();
            row.style.display = textoLinha.includes(termo) ? '' : 'none';
        });
    });
}

function configurarSidebarMobile() {
    const toggle = document.getElementById('sidebarToggle');
    const backdrop = document.getElementById('sidebarBackdrop');

    if (toggle) {
        toggle.addEventListener('click', function () {
            document.body.classList.toggle('sidebar-open');
        });
    }

    if (backdrop) {
        backdrop.addEventListener('click', function () {
            document.body.classList.remove('sidebar-open');
        });
    }
}

function selecionarLinha(linha, seletor) {
    document.querySelectorAll(seletor).forEach(function (l) {
        l.classList.remove('linha-ativa');
    });
    linha.classList.add('linha-ativa');
}

function setValue(id, value) {
    const campo = document.getElementById(id);
    if (campo) campo.value = value || '';
}

function configurarSelecaoCadastros() {
    let linhaSelecionada = null;
    const linhas = document.querySelectorAll('.linha-selecionavel');
    const btnEditar = document.getElementById('btnEditarCadastro');
    const btnExcluir = document.getElementById('btnExcluirCadastro');
    const formEditar = document.getElementById('formEditarCadastro');
    const formExcluir = document.getElementById('formExcluirCadastro');

    if (!linhas.length) return;

    linhas.forEach(function (linha) {
        linha.addEventListener('click', function () {
            selecionarLinha(linha, '.linha-selecionavel');
            linhaSelecionada = linha;
            if (btnEditar) btnEditar.disabled = false;
            if (btnExcluir) btnExcluir.disabled = false;
        });
    });

    if (btnEditar && formEditar) {
        btnEditar.addEventListener('click', function () {
            if (!linhaSelecionada) return;
            const id = linhaSelecionada.dataset.id;
            const tipo = linhaSelecionada.dataset.tipo;
            formEditar.action = `/cadastros/editar/${tipo}/${id}/`;

            setValue('editNome', linhaSelecionada.dataset.nome);
            setValue('editCpfCnpj', linhaSelecionada.dataset.cpfCnpj);
            setValue('editFuncao', linhaSelecionada.dataset.funcao);
            setValue('editNomeFantasia', linhaSelecionada.dataset.nomeFantasia);
            setValue('editEmail', linhaSelecionada.dataset.email);
            setValue('editTelefoneFixo', linhaSelecionada.dataset.telefoneFixo);
            setValue('editCelular', linhaSelecionada.dataset.celular);
            setValue('editCep', linhaSelecionada.dataset.cep);
            setValue('editRua', linhaSelecionada.dataset.rua);
            setValue('editNumero', linhaSelecionada.dataset.numero);
            setValue('editBairro', linhaSelecionada.dataset.bairro);
            setValue('editComplemento', linhaSelecionada.dataset.complemento);
            setValue('editPais', linhaSelecionada.dataset.pais);
            setValue('editUf', linhaSelecionada.dataset.uf);
            setValue('editCidade', linhaSelecionada.dataset.cidade);

            new bootstrap.Modal(document.getElementById('modalEditarCadastro')).show();
        });
    }

    if (btnExcluir && formExcluir) {
        btnExcluir.addEventListener('click', function () {
            if (!linhaSelecionada) return;
            const id = linhaSelecionada.dataset.id;
            const tipo = linhaSelecionada.dataset.tipo;
            formExcluir.action = `/cadastros/excluir/${tipo}/${id}/`;
            const nomeExcluir = document.getElementById('nomeExcluirCadastro');
            if (nomeExcluir) nomeExcluir.innerText = linhaSelecionada.dataset.nome;
            new bootstrap.Modal(document.getElementById('modalExcluirCadastro')).show();
        });
    }
}

function configurarSelecaoProdutos() {
    let linhaSelecionada = null;
    const linhas = document.querySelectorAll('.linha-produto');
    const btnEditar = document.getElementById('btnEditarProduto');
    const btnExcluir = document.getElementById('btnExcluirProduto');
    const formEditar = document.getElementById('formEditarProduto');
    const formExcluir = document.getElementById('formExcluirProduto');

    if (!linhas.length) return;

    linhas.forEach(function (linha) {
        linha.addEventListener('click', function () {
            selecionarLinha(linha, '.linha-produto');
            linhaSelecionada = linha;
            if (btnEditar) btnEditar.disabled = false;
            if (btnExcluir) btnExcluir.disabled = false;
        });
    });

    if (btnEditar && formEditar) {
        btnEditar.addEventListener('click', function () {
            if (!linhaSelecionada) return;
            const id = linhaSelecionada.dataset.id;
            formEditar.action = `/estoque/editar/${id}/`;
            setValue('editProdutoNome', linhaSelecionada.dataset.nome);
            setValue('editProdutoCodigo', linhaSelecionada.dataset.codigo);
            setValue('editProdutoCategoria', linhaSelecionada.dataset.categoriaNome);
            setValue('editProdutoUnidade', linhaSelecionada.dataset.unidade);
            setValue('editProdutoQuantidade', linhaSelecionada.dataset.quantidadeEstoque);
            setValue('editProdutoEstoqueMinimo', linhaSelecionada.dataset.estoqueMinimo);
            setValue('editProdutoPrecoCusto', linhaSelecionada.dataset.precoCusto);
            setValue('editProdutoPrecoVenda', linhaSelecionada.dataset.precoVenda);
            new bootstrap.Modal(document.getElementById('modalEditarProduto')).show();
        });
    }

    if (btnExcluir && formExcluir) {
        btnExcluir.addEventListener('click', function () {
            if (!linhaSelecionada) return;
            const id = linhaSelecionada.dataset.id;
            formExcluir.action = `/estoque/excluir/${id}/`;
            const nomeExcluir = document.getElementById('nomeExcluirProduto');
            if (nomeExcluir) nomeExcluir.innerText = linhaSelecionada.dataset.nome;
            new bootstrap.Modal(document.getElementById('modalExcluirProduto')).show();
        });
    }
}

function configurarSelecaoContas() {
    let linhaSelecionada = null;
    const linhas = document.querySelectorAll('.linha-conta');
    const btnEditar = document.getElementById('btnEditarConta');
    const btnExcluir = document.getElementById('btnExcluirConta');
    const formEditar = document.getElementById('formEditarConta');
    const formExcluir = document.getElementById('formExcluirConta');

    if (!linhas.length) return;

    linhas.forEach(function (linha) {
        linha.addEventListener('click', function () {
            selecionarLinha(linha, '.linha-conta');
            linhaSelecionada = linha;
            if (btnEditar) btnEditar.disabled = false;
            if (btnExcluir) btnExcluir.disabled = false;
        });
    });

    if (btnEditar && formEditar) {
        btnEditar.addEventListener('click', function () {
            if (!linhaSelecionada) return;
            const id = linhaSelecionada.dataset.id;
            formEditar.action = `/contas-pagar/editar/${id}/`;
            setValue('editContaDescricao', linhaSelecionada.dataset.descricao);
            setValue('editContaFornecedor', linhaSelecionada.dataset.fornecedor);
            setValue('editContaValor', linhaSelecionada.dataset.valor);
            setValue('editContaVencimento', linhaSelecionada.dataset.vencimento);
            setValue('editContaStatus', linhaSelecionada.dataset.status);
            setValue('editContaDataPagamento', linhaSelecionada.dataset.dataPagamento);
            setValue('editContaObservacao', linhaSelecionada.dataset.observacao);
            new bootstrap.Modal(document.getElementById('modalEditarConta')).show();
        });
    }

    if (btnExcluir && formExcluir) {
        btnExcluir.addEventListener('click', function () {
            if (!linhaSelecionada) return;
            const id = linhaSelecionada.dataset.id;
            formExcluir.action = `/contas-pagar/excluir/${id}/`;
            const nomeExcluir = document.getElementById('nomeExcluirConta');
            if (nomeExcluir) nomeExcluir.innerText = linhaSelecionada.dataset.descricao;
            new bootstrap.Modal(document.getElementById('modalExcluirConta')).show();
        });
    }
}

// Entrada/Saída/Compra/Venda: em cada modal, se escolher produto no select, limpa busca manual; se digitar busca, limpa select.
document.addEventListener('DOMContentLoaded', function () {
    document.querySelectorAll('.modal').forEach(function (modal) {
        const produtoSelecionado = modal.querySelector('.produto-select-modal');
        const produtoBusca = modal.querySelector('.produto-busca-modal');

        if (!produtoSelecionado || !produtoBusca) return;

        produtoSelecionado.addEventListener('change', function () {
            if (this.value) produtoBusca.value = '';
        });

        produtoBusca.addEventListener('input', function () {
            if (this.value.trim()) produtoSelecionado.value = '';
        });
    });
});

document.addEventListener('DOMContentLoaded', function () {

    const btnLogout = document.getElementById('btnLogout');
    const logoutModal = document.getElementById('logoutModal');
    const btnCancelLogout = document.getElementById('btnCancelLogout');

    if (btnLogout && logoutModal) {

        btnLogout.addEventListener('click', function () {
            logoutModal.classList.add('active');
        });

    }

    if (btnCancelLogout && logoutModal) {

        btnCancelLogout.addEventListener('click', function () {
            logoutModal.classList.remove('active');
        });

    }

    if (logoutModal) {

        logoutModal.addEventListener('click', function (event) {

            if (event.target === logoutModal) {
                logoutModal.classList.remove('active');
            }

        });

    }

});