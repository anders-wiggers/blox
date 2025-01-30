from blox.interfaces.deploy.deployment_strategy import DeploymentStrategy


class PythonDeployer(DeploymentStrategy):
	def deploy(self, source: str):
		print(f"Deploying {source} to Posit Connect")
