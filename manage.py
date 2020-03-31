from app.app import create_app

__author__ = 'Sulayman'

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)
