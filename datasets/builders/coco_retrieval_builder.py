from datasets.builders.base_dataset_builder import BaseDatasetBuilder
from datasets.datasets.retrieval_datasets import RetrievalDataset, RetrievalEvalDataset

from common.registry import registry


@registry.register_builder("coco_retrieval")
class COCORetrievalBuilder(BaseDatasetBuilder):
    train_dataset_cls = RetrievalDataset
    eval_dataset_cls = RetrievalEvalDataset

    def __init__(self, cfg):
        super().__init__(cfg)

    @classmethod
    def default_config_path(cls):
        return "configs/datasets/coco/defaults_ret.yaml"