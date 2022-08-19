from kfp.dsl import ContainerOp


def setup_resources(operator: ContainerOp, memory_request: int, memory_limit: int,
                    cpu_request: int, cpu_limit: int) -> ContainerOp:

    operator.container\
        .set_memory_request(memory_request)\
        .set_memory_limit(memory_limit)\
        .set_cpu_request(cpu_request)\
        .set_cpu_limit(cpu_limit)

    operator.execution_options.caching_strategy.max_cache_staleness = "P0D"

    return operator
