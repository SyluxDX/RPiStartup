alias ..='cd ..'
alias sd='sudo shutdown -h now'
alias rb='sudo shutdown -r now'
alias nano='nano -OSET 4'
alias notes='cat ~/notes.txt'
alias pen='sudo mount /dev/sda1 /media/usb -o uid=pi,gid=pi'
alias upen='sudo umount /media/usb'
alias mount_disk='sudo mount -t ntfs-3g -o uid=pi,gid=pi /dev/sda1 /media/disk/part_a && sudo mount -t ntfs-3g -o uid=pi,gid=pi /dev/sda2 /media/disk/part_b'
alias umount_disk="sudo umount /media/disk/part_a && sudo umount /media/disk/part_b"
