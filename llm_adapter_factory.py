import importlib

def get_llm_adapter(provider, settings):
    """Dynamically import and instantiate the LLMAdapter for the given provider."""
    try:
        module_name = f"{provider}_adapter"
        adapter_module = importlib.import_module(module_name)
        adapter_class = getattr(adapter_module, "LLMAdapter")
        return adapter_class(settings)
    except ModuleNotFoundError:
        raise ValueError(f"No adapter module found for provider: {provider}")
    except AttributeError:
        raise ValueError(f"Module {module_name} does not define 'LLMAdapter'")