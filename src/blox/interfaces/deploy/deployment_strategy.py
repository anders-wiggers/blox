from abc import ABC, abstractmethod


class DeploymentStrategy(ABC):
	@abstractmethod
	def deploy(self, source: str):
		pass
