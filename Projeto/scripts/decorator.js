// Interface que define o contrato para objetos que podem ser decorados
class Component {
    render() {
        throw new Error('render() method must be implemented');
    }
}

// Implementação básica do componente
class IframeComponent extends Component {
    constructor(src) {
        super();
        this.src = src;
    }

    render() {
        return `<iframe width="100%" height="100%" src="${this.src}" style="border: none;" allowfullscreen sandbox="allow-storage-access-by-user-activation allow-scripts allow-same-origin allow-popups allow-popups-to-escape-sandbox"></iframe>`;
    }
}

// Decorator que adiciona um estilo ao componente de iframe
class StyledIframeDecorator extends Component {
    constructor(component, style) {
        super();
        this.component = component;
        this.style = style;
    }

    render() {
        return `<div style="${this.style}">${this.component.render()}</div>`;
    }
}

// Componente que representa a navbar
class NavbarComponent extends Component {
    render() {
        return `
        <nav class="navbar navbar-expand-sm bg-primary">
            <div class="container-fluid">
                <a class="navbar-brand text-white" href="index.html">Alunos por turma</a>
                <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarTogglerDemo01" aria-controls="navbarTogglerDemo01" aria-expanded="false" aria-label="Toggle navigation">
                    <span class="navbar-toggler-icon text-primary"></span>
                </button>
                <div class="collapse navbar-collapse" id="navbarTogglerDemo01">
                    <ul class="navbar-nav">
                        <li class="nav-item">
                            <a class="btn btn-primary" href="mediaalunos.html">Verificar dados</a>
                        </li>
                    </ul>
                </div>
            </div>
        </nav>
        `;
    }
}

// Criar e renderizar os componentes
const iframeComponent = new IframeComponent("https://lookerstudio.google.com/embed/reporting/e99ed38c-902a-4b05-810c-2199dd4e07ca/page/No7tD");
const navbarComponent = new NavbarComponent();
const styledIframeComponent = new StyledIframeDecorator(iframeComponent, "height: calc(100vh - 56px);"); // Subtrai a altura da navbar

// Adiciona a navbar ao corpo do documento
document.body.innerHTML = navbarComponent.render() + styledIframeComponent.render();
