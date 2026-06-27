from services.github_service import GithubService
from dao.repositorio_dao import RepositorioDAO

github = GithubService()

repos = github.obtener_repositorios_objeto("torvalds")

cantidad = RepositorioDAO.guardar_todos("torvalds", repos)

print(f"Guardados: {cantidad}")