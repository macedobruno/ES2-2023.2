// Interface do objeto real
class Subject {
    request() {
        console.log("Subject: Fazendo uma solicitação.");
    }
}

// Objeto real
class RealSubject extends Subject {
    request() {
        console.log("RealSubject: Lidando com a solicitação.");
    }
}

// Proxy
class Proxy extends Subject {
    constructor(realSubject) {
        super();
        this.realSubject = realSubject;
    }

    request() {
        if (this.checkAccess()) {
            this.realSubject.request();
            this.logAccess();
        } else {
            console.log("Proxy: Acesso negado.");
        }
    }

    checkAccess() {
        console.log("Proxy: Verificando permissões de acesso.");
        // Simulação de verificação de acesso
        return true;
    }

    logAccess() {
        console.log("Proxy: Registrando o acesso.");
    }
}

// Uso do Proxy
function clientCode(subject) {
    subject.request();
}

// Exemplo de uso
console.log("Cliente: Chamada direta do objeto real:");
const realSubject = new RealSubject();
clientCode(realSubject);

console.log("");

console.log("Cliente: Chamada do proxy:");
const proxy = new Proxy(realSubject);
clientCode(proxy);
