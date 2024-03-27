// Classe abstrata para a Factory
class FileFactory {
    constructor(data) {
        this.data = data;
    }
    generate() {
        throw new Error("Método generate() deve ser implementado pelas subclasses.");
    }

    // Método estático para criar a fábrica com base no formato
    static createFactory(format, data) {
        switch (format.toLowerCase()) {
            case 'csv':
                return new CSVFactory(data);
            case 'xlsx':
                return new XLSXFactory(data);
            case 'pdf':
                return new PDFFactory(data);
            default:
                throw new Error("Formato inválido.");
        }
    }
}

// Subclasse para geração de arquivos CSV
class CSVFactory extends FileFactory {
    generate() {
        const csvData = Papa.unparse(this.data);
        this.download(csvData, 'text/csv', 'data.csv');
    }
}

// Subclasse para geração de arquivos XLSX
class XLSXFactory extends FileFactory {
    generate() {
        const wb = XLSX.utils.book_new();
        const ws = XLSX.utils.json_to_sheet(this.data);
        XLSX.utils.book_append_sheet(wb, ws, 'Sheet1');
        const xlsxData = XLSX.write(wb, { type: 'blob', bookType: 'xlsx' });
        this.download(xlsxData, 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet', 'data.xlsx');
    }
}

// Subclasse para geração de arquivos PDF
class PDFFactory extends FileFactory {
    generate() {
        const docDefinition = {
            content: this.data
        };
        const pdfData = pdfMake.createPdf(docDefinition).getBlob();
        this.download(pdfData, 'application/pdf', 'data.pdf');
    }
}

// Função para download do arquivo
FileFactory.prototype.download = function(data, type, filename) {
    const blob = new Blob([data], { type: type });
    const url = window.URL.createObjectURL(blob);
    const a = document.createElement('a');
    a.href = url;
    a.download = filename;
    document.body.appendChild(a);
    a.click();
    window.URL.revokeObjectURL(url);
    document.body.removeChild(a);
};

// Função chamada ao clicar nos botões do modal
async function downloadFile(format) {
    // Carregar dados da planilha do Google Sheets 
    const sheetData = await loadGoogleSheet('https://docs.google.com/spreadsheets/d/1NSORDaClmEaWhEgaYV-bWcVZFyKFYJRMl0-UWv_qEOk/edit?usp=sharing');

    // Criar a fábrica com base no formato selecionado
    const factory = FileFactory.createFactory(format, sheetData);
    factory.generate();
}