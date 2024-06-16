key_name               = "my-key-pair"
subnet_id              = "subnet-0bb1c79de"
windows_tags           = {
  Name        = "Windows EC2 Instance"
  Environment = "Production"
  Owner       = "TeamA"
}
ubuntu_tags            = {
  Name        = "Ubuntu EC2 Instance"
  Environment = "Development"
  Owner       = "TeamB"
}
windows_instance_count = 2
ubuntu_instance_count  = 3
instance_type          = "t2.micro"
