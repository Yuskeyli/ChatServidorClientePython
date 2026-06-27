from services.github_service import GithubService

github = GithubService()

repos = github.obtener_repositorios_objeto("torvalds")

print(f"Repositorios encontrados: {len(repos)}")

for repo in repos[:5]:
    print(repo)