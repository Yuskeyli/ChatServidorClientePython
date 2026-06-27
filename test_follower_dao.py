from services.github_service import GithubService
from dao.follower_dao import FollowerDAO

github = GithubService()

followers = github.obtener_followers_objeto("octocat")

cantidad = FollowerDAO.guardar_todos("octocat", followers)

print(f"Followers guardados: {cantidad}")