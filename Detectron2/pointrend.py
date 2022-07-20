import pixellib
from pixellib.torchbackend.instance import instanceSegmentation

ins = instanceSegmentation()
ins.load_model("pointrend_resnet50.pkl")
ins.segmentImage("cycle.jpg", show_bboxes=True, output_image_name="output_point.jpg")
