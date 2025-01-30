from abc import ABC, abstractmethod


class AuthorizeStrategy(ABC):
	@abstractmethod
	def authorize(self, request):
		pass
