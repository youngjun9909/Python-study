package com.korit.fileupload_back.dto;

import lombok.Data;
import org.springframework.web.multipart.MultipartFile;

import java.util.List;

@Data
public class RequestFileUploadDto {
    private String title;
    private List<MultipartFile> img;
}
