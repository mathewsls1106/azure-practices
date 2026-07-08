from django.core.files.uploadedfile import SimpleUploadedFile

from apps.shared.domain.value_objects.file_field_vo import FileFieldVO


class FileFieldMapper:
    @staticmethod
    def file_field_to_vo(file_field) -> FileFieldVO | None:
        if file_field is None:
            return None

        file_field.seek(0)
        file_bytes = file_field.read()

        return FileFieldVO(
            content=file_bytes,
            name=file_field.name,
            size=file_field.size,
        )

    @staticmethod
    def vo_to_file_field(vo: FileFieldVO | None) -> SimpleUploadedFile | None:
        if vo is None:
            return None

        return SimpleUploadedFile(vo.name, vo.content)
